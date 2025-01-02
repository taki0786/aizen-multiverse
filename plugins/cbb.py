#TELEGRAM > @ifeelscam

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text =f"<b>○ 𝐎ᴡɴᴇʀ : <a href='t.me/@DATTEBAYO56'>Dattebayo ֟፝</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Raven'>𝐀ɴɪᴍᴇ Raven</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ : <a href='https://t.me/Anime_Chat_Raven'>𝐀𝐍𝐈𝐌𝐄 Raven</a>\n○ 𝐃ᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/Zorosan110'>Zorosama</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    elif data == "home":
        await query.message.edit_text(
            text=f"𝐊ᴏɴɴɪᴄʜɪᴡᴀ!! 𝐎ᴛᴀᴋᴜ⚡,\n\n<b>ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Multiverse_Hindi'>𝐀ɴɪᴍᴇ 𝐌ᴜʟᴛɪᴠᴇʀsᴇ</a></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data = "about"),
                    InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                ]
            ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    
    elif data == "me":
            await query.message.edit(
                text=f"<b>sᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ʙᴏᴛ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ",url = "https://t.me/Straw_Hat_Bots")],
                        [ InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data = "home"),
                         InlineKeyboardButton( "🚫 ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    
