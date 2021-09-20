import requests
from pyrogram import Client as Bot

from DeCoDeMusic.callsmusic import run
from DeCoDeMusic.config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DeCoDeMusic.handlers")
)

bot.start()
run()
