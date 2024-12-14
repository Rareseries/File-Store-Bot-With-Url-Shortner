import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "23508921"))
  API_HASH = os.environ.get("API_HASH", "70e3ec4bc651ba1c64371003e3c04b6c")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8004400353:AAE5Quuqq0ottoUpZrBpV-Vzrma3DOoZP9c")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Sexy_girlNew_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002392017729"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "https://v2links.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "e86b1065dd994862c9c643e821e10ce48709b87e")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5710180559"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://biswaranjangiri17:biswaranjangiri17@cluster0.spcdm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002459324424")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002389563282"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [ATO](https://t.me/alltypeott)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://i.postimg.cc/VLBW579H/IMG-20241214-170350-555.jpg)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
