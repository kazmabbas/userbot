import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["المطورين","يوسف"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ca7716f51106cd24399ee.jpg",
        caption=f"""• | مطورين سورس ريفز""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "زوكا ", url=f"https://t.me/Q_2_Q_Y"),
                    InlineKeyboardButton(
                        "يوسف ♡", url=f"https://t.me/IC_X_K"),
                ],
                [
                   InlineKeyboardButton(
                        "refz ", url=f"https://t.me/def_Zoka"),
                ],       
            ]
        ),
    )
    