# Stubborn Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Stubborn1223



import os
import sys
import asyncio 
import time, datetime, pytz
from database import db, mongodb_version
from config import Config, temp
from platform import python_version
from translation import Translation
from pyrogram import Client, filters, enums, __version__ as pyrogram_version
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument
from datetime import datetime
TIMEZONE = "Asia/Kolkata"
main_buttons = [[
        InlineKeyboardButton('✇ Uᴘᴅᴀᴛᴇs ✇', url="https://t.me/HGBOTZ"),
        InlineKeyboardButton('✨ 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 ✨', url="https://t.me/Harshit_contact_bot")
    ],[
        InlineKeyboardButton('〄 Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('⍟ Aʙᴏᴜᴛ', callback_data='about')
    ]]     



#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    current_time = datetime.now(pytz.timezone(TIMEZONE))
    curr_time = current_time.hour        
    if curr_time < 12:
         gtxt = "<b>ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ☕</b>" 
    elif curr_time < 17:
         gtxt = "<b>ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ 😈</b>" 
    elif curr_time < 21:
         gtxt = "<b>ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌇</b>"
    else:
         gtxt = "<b>ɢᴏᴏᴅ ɴɪɢʜᴛ 🥱</b>"
    
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
    reply_markup = InlineKeyboardMarkup(main_buttons)
    jishubotz = await message.reply_sticker("CAACAgUAAxkBAAECEEBlLA-nYcsWmsNWgE8-xqIkriCWAgACJwEAAsiUZBTiPWKAkUSmmh4E")
    await asyncio.sleep(2)
    await jishubotz.delete()
    text=Translation.START_TXT.format(user.mention, gtxt)
    await message.reply_photo(
        photo="https://graph.org/file/525c964922c42baeca2f8.jpg", 
        caption=text,
        reply_markup=reply_markup,
        quote=True,
        parse_mode=enums.ParseMode.HTML, 
        has_spoiler=True
    )


#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['restart', "r"]) & filters.user(Config.OWNER_ID))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying To Restarting.....</i>",
        quote=True
    )
    await asyncio.sleep(5)
    await msg.edit("<i>Server Restarted Successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    


#==================Callback Functions==================#

@Client.on_callback_query(filters.regex(r'^help'))
async def helpcb(bot, query):
    await query.message.edit_text(
        text=Translation.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('🛠️ How To Use Me 🛠️', callback_data='how_to_use')
            ],[
            InlineKeyboardButton('⚙️ Settings ⚙️', callback_data='settings#main'),
            InlineKeyboardButton('📊 Stats 📊', callback_data='status')
            ],[
            InlineKeyboardButton('🔙 Back', callback_data='back')
            ]]
        ))



@Client.on_callback_query(filters.regex(r'^how_to_use'))
async def how_to_use(bot, query):
    await query.message.edit_text(
        text=Translation.HOW_USE_TXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🔙 Back', callback_data='help')]]),
        disable_web_page_preview=True
    )



@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await query.message.edit_text(
       reply_markup=reply_markup,
       text=Translation.START_TXT.format(
                query.from_user.first_name, gtxt))



@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_text(
        text=Translation.ABOUT_TXT.format(bot.me.mention),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🔙 Back', callback_data='back')]]),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML,
    )



@Client.on_callback_query(filters.regex(r'^status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    await query.message.edit_text(
        text=Translation.STATUS_TXT.format(users_count, bots_count, temp.forwardings, total_channels, temp.BANNED_USERS ),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🔙 Back', callback_data='help')]]),
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )
    




# Stubborn Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Stubborn1223
