from config import Config
from categorize_answers import (
    analyze_answers_from_file,
    analyze_answer,
    lemmy,
    analysis,
)

import argparse, requests, time, random
from loguru import logger

def tag_new_registrations():
    new_applications = lemmy.get_registration_applications(limit=10)
    for regapp in new_applications:
        if not regapp.get_application_status() == "accepted":
            continue
        if regapp.creator.name in analysis.seen_users:
            continue
        logger.info(f"Categorizing application from user '{regapp.creator.name}'")
        categorize_results = analyze_answer(regapp.answer, regapp.creator.name)
        if not categorize_results["categories_matched"]:
            logger.warning(f"Uncategorized application: {regapp.creator.name}: {regapp.answer}")
            continue
        elif categorize_results["tags_modified"]:
            logger.info(f"Modified tags for {regapp.creator.name}: {categorize_results['tags_modified']}")
        if not categorize_results["user_existed"] or Config.dry_run:
            if not Config.dry_run:
                logger.info("sleeping 60 seconds to allow user cache to expire.")
                time.sleep(61)
            user_req = requests.get(
                f"https://threativore.lemmy.dbzer0.com/api/v1/user/{regapp.creator.name}@lemmy.dbzer0.com"
            )
            tag_markdowns = []
            starting_pack = []
            suggested_comm = {
                "pirate": [
                    "[!piracy@lemmy.dbzer0.com](https://lemmy.dbzer0.com/c/piracy)",            
                    "[!crackwatch@lemmy.dbzer0.com](https://lemmy.dbzer0.com/c/crackwatch@lemmy.dbzer0.com)",            
                ],
                "anarchist": [
                    "[!anarchism@lemmy.dbzer0.com](https://lemmy.dbzer0.com/c/anarchism)",            
                    "[!flippanarchy@lemmy.dbzer0.com](https://lemmy.dbzer0.com/c/flippanarchy)",            
                    "[!leftymemes@lemmy.dbzer0.com](https://lemmy.dbzer0.com/c/leftymemes)",            
                ],
                "foss": [
                    "[!opensource@lemmy.ml](https://lemmy.dbzer0.com/c/opensource@lemmy.ml)",            
                    "[!foss@beehaw.org](https://lemmy.dbzer0.com/c/foss@beehaw.org)",            
                ]
            }
            if user_req.ok:
                tag_markdowns = [
                    f'![{tag["description"]}]({tag["flair"]} "emoji")'
                    for tag in user_req.json().get("tags")
                    if tag["flair"]
                ]
                for tag in user_req.json().get("tags"):
                    if tag["tag"] in suggested_comm:
                        starting_pack += suggested_comm[tag["tag"]]
            intro_msg = (
                f"Welcome to the divisions by zero {regapp.creator.display_name if regapp.creator.display_name else regapp.creator.name}! "
                "\n\nThough parsing your registration application, we have categorized you with the following flair "
                f"{''.join(tag_markdowns)}" 
                "\n\nRemember you can also join our [Matrix Space](https://matrix.to/#/#divisions-by-zero:matrix.org) "
                "and if you are inclined to support our hosting costs, you can fund us on "
                "[Ko-Fi](https://ko-fi.com/dbzer0) or [Liberapay](https://liberapay.com/db0/) which will give you even more flair!"
            )
            if starting_pack:
                intro_msg += (
                    "\n\n---\n\nTo get you started. here's some suggested communities you might like to join:\n\n* "
                    + "\n* ".join(starting_pack) + "\n\nEnjoy!"
            )
            else:
                intro_msg += "\n\nEnjoy!"
            if not Config.dry_run:
                pass
                regapp.creator.pm(content=intro_msg)
            else:
                logger.info(intro_msg)
                admin = lemmy.get_user(username='db0@lemmy.dbzer0.com')
                admin.pm(content=intro_msg)
                break
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze and categorize answers from a file.")
    parser.add_argument('--input_filename', type=str, help='The input file containing answers in JSON format.')
    parser.add_argument('-t', '--tag', action='store_true', help='Enable tagging of users on Threativore.')
    parser.add_argument('--dry_run', action='store_true', help='Only pretend to tag on threativore')
    parser.add_argument('--username', type=str, action='store', help='Pass a username to check what tags would be assigned to it and why')
    args = parser.parse_args()    
    # Override Config values with args if provided
    if args.input_filename:
        Config.input_filename = args.input_filename
    if args.tag is not None:
        Config.enable_tagging = args.tag
    if args.username:
        Config.tag_username = args.username
    if args.dry_run is not None:
        Config.dry_run = args.dry_run
    # Run analysis
    wanted_tagging = Config.enable_tagging
    Config.enable_tagging = False
    analyze_answers_from_file()
    Config.enable_tagging = wanted_tagging
    logger.info("Starting new applications polling loop")
    while True:
        tag_new_registrations()
        time.sleep(Config.new_applications_poll_interval)