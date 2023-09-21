import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID',"23894572")
api_hash = os.environ.get('API_HASH',"bfd6175f254951fa13da6bc1b93d4cb0")
Bot_token = os.environ.get('TOKEN')
Admin= os.environ.get('ADMIN_ID',"689061386")
client=TelegramClient('bot',api_id,api_hash).start(bot_token=Bot_token)
