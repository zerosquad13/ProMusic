
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, emoji

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


    elif query.data=="help":
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
        await query.edit_message_text(
            HELP,
            reply_markup=reply_markup

        )
