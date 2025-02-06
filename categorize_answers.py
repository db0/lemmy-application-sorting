import json
import regex as re
from datetime import datetime
from collections import defaultdict, Counter
from categories import historical_pirates, digital_pirates, foss_advocates, software, anarchists, fictional, other, asd, adhd
from config import Config
from pythorhead import Lemmy
import requests
import argparse
from loguru import logger

lemmy_domain = Config.lemmy_domain
lemmy_username = Config.lemmy_username
lemmy_password = Config.lemmy_password
lemmy = Lemmy(f"https://{lemmy_domain}")
lemmy.log_in(lemmy_username, lemmy_password)

class Analysis:    

    seen_answers: set = set()
    totals: dict
    top_mentions: dict
    seen_users: set = set()

    def __init__(self):
        self.totals = {
            'Historical Pirate': 0,
            'Digital Pirate': 0,
            'Fictional Character': 0,
            'FOSS advocate': 0,
            'Free Software': 0,
            'Anarchist': 0,
            'ASD': 0,
            'ADHD': 0,
            'Other': 0,
            'Total Answers': 0,
            'Multi-category Answers': 0,
            'Unparseable': 0 
        }
        self.top_mentions = {
            category: Counter()
            for category in self.totals 
            if category not in {'Total Answers','Multi-category Answers','Unparseable','ADHD', 'ASD'}
        }

    def get_most_common(self, amount: int = 3):
        # Show the top 3 results per category
        most_common = {}
        for category in self.top_mentions:
            most_common[category] = analysis.top_mentions[category].most_common(amount)
        return most_common

analysis = Analysis()

def convert_categories_to_threativore_tags(categories: dict) -> list[dict]: 
    tags_list = []
    for cat in categories:
        if cat in ['Historical Pirate', 'Fictional Character', 'Digital Pirate']:
            tags_list.append({"tag": "pirate","value": "true"})
        if cat in ['FOSS advocate', 'Free Software']:
            tags_list.append({"tag": "foss","value": "true"})
        if cat in ['Anarchist']:
            tags_list.append({"tag": "anarchist","value": "true"})
        if cat in ['Other']:
            tags_list.append({"tag": "snowflake","value": "true"})
        if cat in ['ASD']:
            tags_list.append({"tag": "asd","value": "true"})
        if cat in ['ADHD']:
            tags_list.append({"tag": "adhd","value": "true"})
    return tags_list

def are_all_local_tags_in_threativore(local_tags: list[dict], threativore_tags: list[dict]):
    # logger.debug(local_tags)
    # logger.debug(threativore_tags)
    for local_tag in local_tags:
        match = next((t for t in threativore_tags if t['tag'] == local_tag['tag'] and t['value'] == local_tag['value']), None)
        
        if not match:
            return False
    return True

def add_threativore_tags(username, categories, is_first = False) -> bool:
    "Returns True if threativore edited. Else returns False"

    known_bypasses = {
        "martineski": {"tag": "foss","value": "true"}
    }
    if username.lower() in known_bypasses:
        tags = [known_bypasses[username.lower()]]
    else:
        tags = convert_categories_to_threativore_tags(categories)
    if is_first:
        tags.append({"tag": "first","value": "true"})        
    user_req = requests.get(
        f"https://threativore.lemmy.dbzer0.com/api/v1/user/{username}@lemmy.dbzer0.com"
    )
    if not tags: 
        logger.info(f"No flair found for {username}")
        return {"tags_modified":False, "user_existed": user_req.status_code == 200}
    request_func = requests.patch
    if user_req.status_code == 404:
        request_func = requests.put
    elif user_req.status_code == 200:
        user_deets = user_req.json()
        if are_all_local_tags_in_threativore(tags, user_deets.get("tags")):
            logger.info(f"All flair tags already set for {username}")
            return {"tags_modified":False, "user_existed": True}
    if not Config.dry_run:
        user_mod_req = request_func(
            f"https://threativore.lemmy.dbzer0.com/api/v1/user/{username}@lemmy.dbzer0.com",
            headers={"apikey": Config.threativore_api_key},
            json={"tags": tags},
        )
        user_mod_req.raise_for_status()
    tag_values = [tag['tag'] for tag in tags]
    logger.info(f"flair tags {tag_values} set for {username}")
    return {"tags_modified":True, "user_existed": user_req.status_code == 200}
        

def normalize_mention(mention):
    # Normalize mentions like 'Linus' and 'Torvalds' to 'Linus Torvalds'
    mention = mention.lower()
    if mention == r'(linus|torvalds)':
        return "Linus Torvalds"
    if mention == r'(stall?man|\brms\b)':
        return "Richard Stallman"
    if mention == r'ross?man':
        return "Louis Rossmann"
    if mention == r'(b[kl]ack.{0,20}beard|teach)':
        return "Blackbeard"
    if mention == r'anne.{0,10}bonny':
        return "Anne Bonny"
    if mention == r'[cz]h[ie]ng (y?i )?(sao|shih)':
        return "Zheng Yi Sao"
    if mention == r'fi[rt][ -]?(bit)? ?girl':
        return "fitgirl"
    if mention == r'(goldman|red emma)':
        return "Emma Goldman"
    if mention == r'(swartz?|schwarz)':
        return "Aaron Swartz"
    if mention == r'dread ?pirate ?roberts?':
        return "Dread Pirate Robers"
    if mention == r'\bgnu\b':
        return "GNU"
    if mention == r'(sparrow|johnny depp|pirates.{0,10}car?ribb?ean)':
        return "Captain Jack Sparrow"
    if mention == r'(pirate.{0,10}bay|tpb)':
        return "The Pirate Bay"
    if mention == r'anon(ymo?us)?':
        return "Anonymous"
    return mention

def categorize_mentions(answer):
    # Convert answer to lowercase for case-insensitive matching
    try:
        answer_lower = answer.lower().encode('utf-8').decode('utf-8')
    except UnicodeDecodeError as err:
        logger.debug(f"Could not decode: {answer.lower()}")
        answer_lower = answer.lower()
    
    # Initialize results for counting
    found_categories = defaultdict(list)
    is_first = False
    # Check each category
    seek_cat = {
        'Historical Pirate': historical_pirates,
        'Fictional Character': fictional,
        'Digital Pirate': digital_pirates,
        'FOSS advocate': foss_advocates,
        'Free Software': software,
        'Anarchist': anarchists,
        'ASD': asd,
        'ADHD': adhd,
    }    

    for category_name, category in seek_cat.items():
        for seek in category:
            try:
                if re.search(seek,answer_lower, re.RegexFlag.IGNORECASE):
                    if Config.tag_username:
                        logger.info(f"Matched {category_name}: {seek}")
                    found_categories[category_name].append(seek)
                    if seek not in analysis.seen_answers and category_name not in {'ASD', 'ADHD'}:
                        analysis.seen_answers.add(seek)
                        is_first = True
                    break
            except Exception as err:
                logger.error(f"Error in search: {seek}")
                raise err

    # Random stuff don't get a first
    for thing in other:
        if re.search(thing, answer_lower, re.RegexFlag.IGNORECASE):
            found_categories['Other'].append(thing)
    
    return found_categories, is_first

def get_categories_without_neurodivergence(categories):
    return {k:v for k,v in categories.items() if k not in {'ASD', 'ADHD'}}

def analyze_answer(answer, username):
    # Get categories for this answer and updates the totals
    # Return dict with bools of whether categories were matched and tags were modified
    categories, is_first = categorize_mentions(answer)
    # Count how many categories this answer matches
    categories_matched = sum(1 for v in categories.values() if v)
    non_nd_categories = get_categories_without_neurodivergence(categories)
    non_nd_categories_matched = sum(1 for v in non_nd_categories.values() if v)
    
    if Config.tag_username and username == Config.tag_username:
        logger.info(f"found {Config.tag_username} with answer: {answer}")

    if categories_matched == 0:
        return {
            "categories_matched": False,
            "non_nd_categories_matched": False,
            "tags_modified": False, 
            "user_existed": False
        }
    elif non_nd_categories_matched > 1:
        analysis.totals['Multi-category Answers'] += 1
    
    # Update totals and track top mentions
    for category, mentions in categories.items():
        if mentions:
            analysis.totals[category] += 1
            normalized_mentions = [normalize_mention(mention) for mention in mentions]
            try:
                if category in analysis.top_mentions:
                    analysis.top_mentions[category].update(normalized_mentions)
            except Exception as err:
                logger.error([category,analysis.top_mentions])
                raise err
    opret = {}
    if Config.enable_tagging:
        opret = add_threativore_tags(username, categories, is_first)
    return {
        "categories": categories,
        "non_nd_categories": non_nd_categories,
        "non_nd_categories_matched": non_nd_categories_matched > 0,
        "categories_matched": True, 
        "tags_modified": opret.get("tags_modified", False), 
        "user_existed": opret.get("user_existed", False)
    }

def analyze_answers_from_file():

    
    uncategorized = []
    uncategorized_full = []
    
    
    try:
        with open(Config.input_filename, 'r') as file:
            
            l = 0
            line_nr = 0
            for line in file:
                line_nr += 1
                try:
                    data = json.loads(line.strip().replace('\\\\','\\').replace('\\n',' ').replace('\n',' '))
                    answer = data['answer']
                    username = data['username']
                    if Config.tag_username and username != Config.tag_username:
                        continue
                    analysis.seen_users.add(username)                    
                    analysis.totals['Total Answers'] += 1
                    categorize_results = analyze_answer(answer, username)
                    if not categorize_results["categories_matched"]:
                        uncategorized.append(answer)
                        uncategorized_full.append(data)
                    elif categorize_results["tags_modified"]:
                        l += 1
                    if Config.debug_lines > 0 and l >= Config.debug_lines: # Debug
                        break
                except json.JSONDecodeError:
                    logger.warning(f"unparseable line {line_nr}")
                    logger.debug(line.strip().replace('\\\\','\\').replace('\\n',''))
                    analysis.totals['Unparseable'] += 1
   
    except FileNotFoundError:
        logger.error(f"Error: Could not find file {Config.input_filename}")
        return None, None
        
    logger.info(f"{l} entres edited on threativore")
    # Write uncategorized answers to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{Config.output_filename}_{timestamp}.txt"
    uncat_json = f"{Config.output_filename}_full_{timestamp}.json"
    
    with open(uncat_json, 'w') as f:
        json.dump(uncategorized_full, f, indent=4)
    
    with open(output_file, 'w') as f:
        f.write("Uncategorized Answers:\n")
        f.write("---------------------\n")
        for idx, answer in enumerate(uncategorized, 1):
            f.write(f"{idx}. {answer}\n")
    
    return output_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze and categorize answers from a file.")
    parser.add_argument('--input_filename', type=str, help='The input file containing answers in JSON format.')
    parser.add_argument('-t', '--tag', action='store_true', help='Enable tagging of users on Threativore.')
    parser.add_argument('--dry_run', action='store_true', help='Only pretend to tag on threativore')
    parser.add_argument('-d', '--debug_lines', type=int, help='Number of lines to process for debugging purposes.')
    parser.add_argument('--username', type=str, action='store', help='Pass a username to check what tags would be assigned to it and why')
    args = parser.parse_args()
    # Override Config values with args if provided
    if args.input_filename:
        Config.input_filename = args.input_filename
    if args.tag is not None:
        Config.enable_tagging = args.tag
    if args.dry_run is not None:
        Config.dry_run = args.dry_run
    if args.debug_lines:
        Config.debug_lines = args.debug_lines
    if args.username:
        Config.tag_username = args.username
    # Run analysis
    output_file = analyze_answers_from_file()
    if Config.tag_username:
        exit(0)    
    if analysis.totals:
        print("\nAnalysis Results:")
        print("-----------------")
        for category, count in analysis.totals.items():
            if category not in ['Total Answers', 'Multi-category Answers']:
                percentage = (count / analysis.totals['Total Answers']) * 100
                print(f"{category}: {count} ({percentage:.1f}%)")
        
        print(f"\nTotal Answers Analyzed: {analysis.totals['Total Answers']}")
        print(f"Answers matching multiple categories: {analysis.totals['Multi-category Answers']}")
        
        print("\nTop Mentions per Category:")
        print("---------------------------")
        for category, mentions in analysis.get_most_common().items():
            mention_display = [f"{mention.title()} ({count})" for mention, count in mentions]
            print(f"{category}: {', '.join(mention_display)}")
        
        print(f"\nUncategorized answers have been written to: {output_file}")

