import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID',"1464463")
api_hash = os.environ.get('API_HASH',"ff8451462d91861a13ffd8a6bb72aa8b")
Bot_token = os.environ.get('TOKEN',"6344846447:AAEqnJhFGrZE4auYKHTijHETVsBR6kcJaP0")
Admin= os.environ.get('ADMIN_ID',"689061386")
client=TelegramClient('bot',api_id,api_hash).start(bot_token=Bot_token)
