# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28993806")

API_HASH = os.environ.get("API_HASH", "a361bd7ea5fb4930786e54a480a6e929")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7378927068:AAFxQLy6jDFSJ7bL3FSCCab78Lki5bFhVVg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "DS_WORLD") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamebot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://santhusugu33:6NouR90tLF1pJBSL@dsworld.dil3c.mongodb.net/?retryWrites=true&w=majority&appName=Dsworld")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5100745828').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
