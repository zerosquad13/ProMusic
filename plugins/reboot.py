from pyrogram import Client, filters
from handlers import check_heroku
from helpers.decorators import sudo_users_only


@Client.on_message(filters.command("restart") & filters.user(870471128))
@sudo_users_only
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_photo(
                                     photo="https://te.legra.ph/file/f412a0a94c1da161a7013.jpg", 
                                     caption="**Restaring**\n**Please Wait...**"
   )
    hap.restart()
