from pyrogram import Client, filters

@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "about"
        await msg.answer("""🕹️ Bot Type :  Pyrogram Tester
⚙️ Language : Python 3.9.9
📚 Library : Pyrogram Asyncio 1.13.0 
🖲️Server : Oktato / Railway
🧮 Base Source Code : CominSoon""", show_alert=True)
