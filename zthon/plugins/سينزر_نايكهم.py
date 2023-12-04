#refz ®
#الملـف حقـوق وكتابـة المبرمج سينزر
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from zthon import zedub

from ..core.managers import edit_or_reply



@zedub.zed_cmd(pattern="كسم عقرب  ?(.*)")
async def zilzal(event):
    card = event.pattern_match.group(1)
    chat = "@PlayGgbot"
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**جاري البحث انتظر قليلا ... 💡**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("@PlayGgbot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()
