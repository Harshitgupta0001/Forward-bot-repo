# Stubborn Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Stubborn1223


import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002166149059').split()] 
class Config:
    API_ID = os.environ.get("API_ID", "29940662")
    API_HASH = os.environ.get("API_HASH", "b9ccc26a417ce3a998d321086a2edbb6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6748961187:AAFMdcvheBBL_Yqv6QpwHb11Iw0-Ej2RINA") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://david:surya@cluster12.f7tpy44.mongodb.net/")
    DB_NAME = os.environ.get("DB_NAME", "Stubborn")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '6359874284').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    






# Stubborn Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Stubborn1223
