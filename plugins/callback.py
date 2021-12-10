from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import BOT_USERNAME
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery



@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**DeeCode Music Bot : Help Menu**

__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__

**🏷 Common Commands!

/play<song name> to play song from. YouTube 
/audio - reply to audio file/YouTube link to play
/pause - to pause currently stream
/resume - to resume currently paused
/skip || /next - to change song(work only  if another song is in queue) 
/end|| /stop - stop/ends music Stream
/refresh || /restart - to restart Bot Server(only for heroku) 

/update - to update latest version From Git.
/ping - to see network speed """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/DeCodeSupport"),
                    InlineKeyboardButton(text="📣 Channel", url=f"https://t.me/TeamDeeCoDe")
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
    f"""<b>👋 𝙃𝙀𝙇𝙇𝙊 𝙏𝙃𝙀𝙍𝙀 ❗ 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙈𝙔 𝘽𝙊𝙏💞

𝙏𝙃𝙄𝙎 𝙄𝙎 𝘼 𝘽𝙊𝙏 𝘿𝙀𝙎𝙄𝙂𝙉𝙀𝘿 𝙏𝙊 𝙋𝙇𝘼𝙔 𝙈𝙐𝙎𝙄𝘾 𝙄𝙉 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋𝙎!

𝙃𝙀𝙍𝙀 𝘼𝙍𝙀 𝙎𝙊𝙈𝙀 𝘾𝙈𝘿𝙎 𝙏𝙊 𝙐𝙎𝙀 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕Summon Me➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)
                  ],[
                    InlineKeyboardButton(
                       "🗣️ Support 🗣️", url="https://t.me/DeCodeSupport"
                    ),
                    InlineKeyboardButton(
                        "📣 Updates 📣", url="https://t.me/TeamDeeCoDe")
                ],[
                    InlineKeyboardButton(
                        "📚 Commands", callback_data="cbcmds"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
