from environs import Env
env = Env()
env.read_env()  # read .env file, if it exists

class Config:
    lemmy_domain: str = env.str("LEMMY_DOMAIN")
    lemmy_username: str = env.str("LEMMY_USERNAME")
    lemmy_password: str = env.str("LEMMY_PASSWORD")
    threativore_api_key: str = env.str("THREATIVORE_API_KEY")
    input_filename: str = env.str("INPUT_FILENAME", "registration_answers.json")
    output_filename: str = env.str("OUTPUT_FILENAME", "uncategorized_answers")
    enable_tagging: bool = env.bool("ENABLE_TAGGING", False)
    debug_lines: int = env.int("DEBUG_LINES", 0)
    tag_username: str = env.str("TAG_USERNAME", "")
    new_applications_poll_interval: int = env.int("NEW_APPLICATIONS_POLL_INTERVAL", 1800)
    dry_run: bool = env.bool("DRY_RUN", False)
    force_pm: bool = env.bool("FORCE_PM", False)
    store_answers: bool = env.bool("STORE_ANSWERS", True)