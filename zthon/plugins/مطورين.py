import zthon
from zedthon import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from zedthon import zedthon


@app.on_message(
    command(["المطورين","اعدام"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ad825b5bc2c0285006e2b.jpg",
        caption=f"""• | مطورين سورس القائد""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "منذر ", url=f"https://t.me/Z_X_Z_B"),
                    InlineKeyboardButton(
                        "اعدام ♡", url=f"https://t.me/DAD_E3DAM"),
                ],
                [
                   InlineKeyboardButton(
                        "Leader ", url=f"https://t.me/V_P_N_8"),
                ],       
            ]
        ),
    )
    
