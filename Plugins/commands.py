from pyrogram import Client, filters


START_MESSAGE = """ʜᴇy {}, ɪ ᴀᴍ ᴀ ꜱᴩᴇᴄɪᴀʟ ʙᴏᴛ ꜰᴏʀ ᴩyʀᴏɢʀᴀᴍ ᴛᴇꜱᴛ
"""


@Client.on_message(filters.command("start")
async def start_cmd(bot, msg):
    await msg.reply_photo(
       photo="https://telegra.ph/file/d6e93a4e09f7993b12fa5.jpg",
       caption=START_MESSAGE.format(msg.from_user.mention),
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("🧛Dᴇᴠ", url="t.me/pushpa_reju")
            
           ]]
           )
    )
