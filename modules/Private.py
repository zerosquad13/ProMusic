from time import time
from datetime import datetime
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from pyrogram import Client, filters
import signal
import os
import sys

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\n• Iam A Bot Project by @TGBOTZXD\n• I Can Manage Group VC's\n\n• Hit /help to know about available commands.</b>"
HELP = """
🎧 <b>I Can Play Musics On VoiceChats 🤪</b>

🎶 **Common Commands**:
• `/song` __Download Song from youtube__
• `/play`  __Play song you requested__
• `/help` __Show help for commands__
• `/dplay` __Play song you requested via deezer__
• `splay` __Play song you requested via jio saavn__
• `/ytplay` __Play song directly from youtube server__
• `/search` __Search video songs links__
• `/current` __Show now playing__
• `/playlist` __Show now playing list__
• `/video` __Downloads video song quickly__
🎶 **Admin Commands**:
• `/player`  __Open music player settings panel__
• `/pause` __Pause song play__
• `/skip` __Skip next song__
• `/resume`  __Resume song play__
• `/userbotjoin`  __Invites assistant to your chat__
• `/end` __Stops music play__
• `/admincache` __Refresh list of admins with vc power__
© Powered By 
[ __@tgbotsXD || @tgbotzXD__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('📢 Updates', url='https://t.me/TGBOTZXD'),
                InlineKeyboardButton('💬 Support', url='https://t.me/TGBOTSXD')
                ],[
                InlineKeyboardButton('🤖 Developer', url='https://t.me/piroXpower'),
                InlineKeyboardButton('🎧 Chats', url='https://t.me/frndsXworld')
                ],[
                InlineKeyboardButton('📜 Source Code 📜', url='https://github.com/TEAM-PATRICIA/PatriciaMusic2.0'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/33cc1aeaf934f19943bdc.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('📢 Updates', url='https://t.me/TGBOTZXD'),
                InlineKeyboardButton('💬 Support', url='https://t.me/TGBOTSXD')
                ],[
                InlineKeyboardButton('🤖 Developer', url='https://t.me/piroXpower'),
                InlineKeyboardButton('🎧 Chats', url='https://t.me/frndsXworld')
                ],[
                InlineKeyboardButton('📜 Source Code 📜', url='https://github.com/TEAM-PATRICIA/PatriciaMusic2.0'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/33cc1aeaf934f19943bdc.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
