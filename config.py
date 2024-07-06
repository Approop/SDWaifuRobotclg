import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    BOT_TOKEN = os.getenv("7009368458:AAGTbzViA1r8iReHrCYns7EHx0Ezh9L3BIM")
    API_ID = os.getenv("22758382")
    API_HASH = os.getenv("328b4e55c6a0e1d72534329a27fc0d90")
    mediaPattern = r"\b(https?://(?:(.*?)\.)?(?:instagram\.com|www\.instagram\.com|t\.co|twitter\.com|x\.com|pin\.it|pinterest\.com|in\.pinterest\.com)(?:[^\s]*))\b"
