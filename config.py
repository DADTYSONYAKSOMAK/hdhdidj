import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 23464711))

    API_HASH = os.environ.get("API_HASH", "d18596102470dff56b5f6c0c9844519e")

    