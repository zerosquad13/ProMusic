import requests
from pyrogram import Client as Bot

from DeCodeMusic.callsmusic import run
from DeCodeMusic.config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DeCodeMusic.handlers")
)

bot.start()
run()
