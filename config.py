import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", '')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 12345))
    CHAT = int(os.environ.get("CHAT", "-1001541558103"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001541558103")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("API_HASH", "d5095c6ebd89c728289cec4bb91941b7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2029745374:AAE32ZlkKeewZjxUwTfsQk_swrd5JoT-0yo") 
    SESSION = os.environ.get("SESSION_STRING", "")

