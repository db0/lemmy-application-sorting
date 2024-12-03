import json
from config import Config
import requests

import argparse
parser = argparse.ArgumentParser(description="Analyze and categorize answers from a file.")
parser.add_argument('input_filename', type=str, nargs='?', default='registration_answers_early_birds.json', help='The input file containing answers in JSON format.')

args = parser.parse_args()


def are_all_local_tags_in_threativore(local_tags: list[dict], threativore_tags: list[dict]):
    for local_tag in local_tags:
        match = next((t for t in threativore_tags if t['tag'] == local_tag['tag'] and t['value'] == local_tag['value']), None)
        
        if not match:
            return False
    return True

def add_early_bird_tag(username) -> bool:
    
    "Returns True if threativore edited. Else returns False"
    tags = [{"tag": "early_bird","value": "true"}]
    user_req = requests.get(
        f"https://threativore.lemmy.dbzer0.com/api/v1/user/{username}@lemmy.dbzer0.com"
    )
    request_func = requests.patch
    if user_req.status_code == 404:
        request_func = requests.put
    else:
        user_deets = user_req.json()
        if are_all_local_tags_in_threativore(tags, user_deets.get("tags")):
            print(f"All flair tags already set for {username}")
            return False
    user_mod_req = request_func(
        f"https://threativore.lemmy.dbzer0.com/api/v1/user/{username}@lemmy.dbzer0.com",
        headers={"apikey": Config.threativore_api_key},
        json={"tags": tags},
    )
    user_mod_req.raise_for_status()
    tag_values = [tag['tag'] for tag in tags]
    print(f"flair tags {tag_values} set for {username}")
    return True

def analyze_early_birds(input_filename):
    try:
        total = 0
        with open(input_filename, 'r') as file:
            for line in file:
                data = json.loads(line.strip())
                if add_early_bird_tag(data['username']):
                    total += 1
    except FileNotFoundError:
        print(f"Error: Could not find file {input_filename}")
        return None, None
    print(f"Total early birds added this run: {total}")
    
analyze_early_birds(args.input_filename)
