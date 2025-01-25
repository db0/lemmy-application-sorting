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
    new_applications = lemmy.get_registration_applications(limit=30)
    for regapp in new_applications:
        if not regapp.get_application_status() == "accepted":
            continue
        if regapp.creator.name in analysis.seen_users:
            continue
        if Config.tag_username and regapp.creator.name != Config.tag_username:
            continue
        categorize_results = analyze_answer(regapp.answer, regapp.creator.name)
        if not categorize_results["categories_matched"]:
            logger.warning(f"Uncategorized application: {regapp.creator.name}: {regapp.answer}")
            continue
        elif categorize_results["tags_modified"]:
            logger.info(f"Modified tags for {regapp.creator.name}: {categorize_results['tags_modified']}")
        analysis.seen_users.add(regapp.creator.name)
        if not categorize_results["user_existed"] or Config.dry_run or Config.force_pm == regapp.creator.name:
            if not Config.dry_run:
                logger.info("sleeping to allow user cache to expire.")
                time.sleep(61)
            user_req = requests.get(
                f"https://threativore.lemmy.dbzer0.com/api/v1/user/{regapp.creator.name}@lemmy.dbzer0.com"
            )
            tag_markdowns = []
            starting_pack = []
            suggested_comm = {
                "pirate": [
                    "[Piracy](https://lemmy.dbzer0.com/c/piracy)",
                    "[Crackwatch](https://lemmy.dbzer0.com/c/crackwatch@lemmy.dbzer0.com)",
                ],
                "anarchist": [
                    "[Anarchism](https://lemmy.dbzer0.com/c/anarchism)",
                    "[Flippanarchy](https://lemmy.dbzer0.com/c/flippanarchy)",
                    "[Lefty Memes](https://lemmy.dbzer0.com/c/leftymemes)",
                ],
                "foss": [
                    "[Open Source](https://lemmy.dbzer0.com/c/opensource@lemmy.ml)",
                    "[FOSS](https://lemmy.dbzer0.com/c/foss@beehaw.org)",
                ],
                "adhd": [
                    "[ADHD Memes](https://lemmy.dbzer0.com/c/adhd)",
                    "[ADHD](https://lemmy.dbzer0.com/c/adhd@lemmy.world)",
                ],
                "asd": [
                    "[Ausome Memes](https://lemmy.dbzer0.com/c/ausomememes)",
                    "[Autism](https://lemmy.dbzer0.com/c/autism)",
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
                "\n\nThrough parsing your registration application, we have assigned you the following flair "
                f"{''.join(tag_markdowns)}" 
                "\n\nRemember you can also join our [Matrix Space](https://matrix.to/#/#divisions-by-zero:matrix.org) "
                "and if you are inclined to support our hosting costs, you can fund us on "
                "[Ko-Fi](https://ko-fi.com/dbzer0) or [Liberapay](https://liberapay.com/db0/) which will give you even more flair!"
            )
            if starting_pack:
                intro_msg += (
                    "\n\n---\n\nTo get you started. here's some suggested communities you might like to join:\n\n* "
                    + "\n* ".join(starting_pack)
                    + "\n\nYou can also discover thousands of communities on the [Lemmyverse](https://lemmyverse.net/communities)\n\nEnjoy!"
                )
            else:
                intro_msg += "\n\nYou can also discover thousands of communities on the [Lemmyverse](https://lemmyverse.net/communities)\n\nEnjoy!"

            if not Config.dry_run:
                logger.info(f"Sending Welcome PM to {regapp.creator.name}")
                regapp.creator.pm(content=intro_msg)
            else:
                logger.info(intro_msg)
                # admin = lemmy.get_user(username='db0@lemmy.dbzer0.com')
                # admin.pm(content=intro_msg)
                exit(0)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze and categorize answers from a file.")
    parser.add_argument('--input_filename', type=str, help='The input file containing answers in JSON format.')
    parser.add_argument('-t', '--tag', action='store_true', help='Enable tagging of users on Threativore.')
    parser.add_argument('--dry_run', action='store_true', help='Only pretend to tag on threativore')
    parser.add_argument('--force_pm', type=str, action='store', help='Pass a username which will receive a forced welcome PM when detected')
    parser.add_argument('--username', type=str, action='store', help='Pass a username to check what tags would be assigned to it and why')
    args = parser.parse_args()    
    # Override Config values with args if provided
    if args.input_filename:
        Config.input_filename = args.input_filename
    if args.tag is not None:
        Config.enable_tagging = args.tag
    if args.dry_run is not None:
        Config.dry_run = args.dry_run
    if args.username is not None:
        Config.tag_username = args.username
    if args.force_pm is not None:
        Config.force_pm = args.force_pm
    # Run analysis
    wanted_tagging = Config.enable_tagging
    Config.enable_tagging = False
    analyze_answers_from_file()
    Config.enable_tagging = wanted_tagging
    logger.info("Starting new applications polling loop")
    while True:
        tag_new_registrations()
        if args.force_pm is not None:
            break
        time.sleep(Config.new_applications_poll_interval)