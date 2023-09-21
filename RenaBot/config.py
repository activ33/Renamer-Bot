import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
Bot_token = os.environ.get('TOKEN',"6404643240:AAFCTb03FBn34kMVqaagNyj9tkyjGW6G5P0")
Admin= os.environ.get('ADMIN_ID',"689061386")
client=TelegramClient('bot',api_id,api_hash).start(bot_token=Bot_token)
