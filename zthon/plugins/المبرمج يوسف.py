# refz - yousef
# Copyright (C) 2022 refz . All Rights Reserved
#< https://t.me/def_Zoka >
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.

import json
import math
import os
import aiohttp
import requests
import random
import re
import time
from uuid import uuid4
import sys
import asyncio
from validators.url import url
from subprocess import run as runapp
from datetime import datetime
from pySmartDL import SmartDL
from pathlib import Path
from platform import python_version
from telethon import Button, functions, events ,types, version
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery
from telethon.utils import get_display_name
from telethon.tl.types import InputMessagesFilterDocument
from zthon import StartTime, zedub, zedversion
from ..Config import Config
from ..helpers.functions import rand_key
from ..core import check_owner, pool
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..helpers.utils import reply_id, get_user_from_event, _format
from ..helpers.tools import media_type
from . import media_type, progress
from ..utils import load_module, remove_plugin
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, BOTLOG, BOTLOG_CHATID, HEROKU_APP, mention


LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ZORDR = gvarstatus("Z_ORDR") or "مط"
ZLORDR = gvarstatus("Z_LORDR") or "مط"
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
cmdhd = Config.COMMAND_HAND_LER
DELETE_TIMEOUT = 1
USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
Malath = f"**☆┊لـَوحـة أوامـِر َِᖇُِ꧖َِƒُِᤁالشفـافَـة**\n**☆┊المستخـِدم ↶** {mention} \n\n ١**    ۦ اوامــࢪ الـبحـث والـتحميـل **\n ٢**    ۦ اوامــࢪ الـبـوت **\n ٣**    ۦ اوامــࢪ الـوقـتـي **\n ٤**    ۦ اوامــࢪ الـڪــروب¹ **\n ٥**    ۦ اوامــࢪ الـڪــروب² **\n ٦**    ۦ اوامــࢪ الحـسـاب **\n ٦**    ۦ اوامــࢪ الميـديـا والصيــغ **\n\n**•-⛥⤻ لـ؏ـࢪض بقـية الأوامـر اضـغط زࢪ⇒**\n**-المطورين** `.`\n**مطورين ريفز` "
Malotha = f"**‌‌‏⚚┃ يتبـع لـوحـة أوامـࢪ َِᖇُِ꧖َِƒُِᤁالشفـافـَة**\n**‌‌‏⚚┃ المستخـِدم -** {mention} \n\n- ٨ ⪧** اوامـِـࢪ الـفــارات **\n- ٩ ⪧** اوامـِـࢪ الخـدمــات الـعامــة **\n- ١٠ ⪧** اوامـِـࢪ الالعــاب **\n- ١١ ⪧** اوامـِـࢪ الـتســليــه**\n- ١٢ ⪧** اوامـِـࢪ التحشيـش**\n- ١٣ ⪧** اوامـِـࢪ الستـوريات**\n- ١٤ ⪧•** اوامـِـࢪ الآفتــارات**\n\n**-‌‌‏⚚⤶ للذهـاب للـوحـة التـاليـة اضغـط زࢪ ⤻  ᯽. **\n**-⛥⤻ لعـرض الأوامِـࢪ مع الوصـِف أرسل** `.اوامري`\n**- ⛥⤻ لعـرض شـِروحـَات الأوامـر أࢪسـِل** `.مساعده` "
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Channels = f"**•❐•  مرحبـًا عـزيـزي  {mention} **\n**•❐• إليـك مجمـوعــة قنـوات ريفز ↵ َِᖇُِ꧖َِƒُِᤁ ♥️🧸**\n\n**•❐• استـخـدم الازرار بالاسفــل↓**"
Zelzal = f"**•◈• إصــدار الســورس ⤽ 2.0**  \n**•◈• المستخــدم ⤽**  {mention}  \n**•◈• وقــت التشغيــل ⤽  {TM}  **\n**•◈• البــوت المســاعـد ⤽  {TG_BOT} **\n**•◈• قنــاة الســورس ⤽  @def_Zoka **"
TGT_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Channels = f"**•❐• مرحبًـا عـزيـزي  {mention} **\n**•❐• إليـك مجمـوعــة قنـوات ريفز ↵ َِᖇُِ꧖َِƒُِᤁ ♥️🧸**\n\n**•❐• استـخـدم الازرار بالاسفــل↓**"
Zelzal = f"**•◈• إصــدار الســورس ⤽ 2.0**  \n**•◈• المستخــدم ⤽**  {mention}  \n**•◈• وقــت التشغيــل ⤽  {TM}  **\n**•◈• البــوت المســاعـد ⤽  {TGT_BOT} **\n**•◈• قنــاة الســورس ⤽  @def_Zoka **"


#لـوحــة الاوامـِـࢪ - حقــوق تيبثـون - الكـاتب زلـزال الهـيبـة
@zedub.tgbot.on(events.InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("الاوامر") and event.query.user_id == zedub.uid:
        buttons = [[Button.inline("⛥ ١", data="ahmed1"), Button.inline("يوسف", data="ahmed2"), Button.inline("سينزر", data="ahmed3"), Button.inline("سينزر", data="ahmed4"),],[Button.inline("", data="ahmed5"), Button.inline("⛥ ٦", data="ahmed6"), Button.inline("⛥ ٧", data="ahmed7"), Button.inline("⇒", data="back1"),]]
        result = builder.article(title="zedub",text=Malath,buttons=buttons,link_preview=False)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="الاوامر(?: |$)(.*)")
async def repozedub(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await event.client.inline_query(Config.TG_BOT_USERNAME, "مط")
    await response[0].click(event.chat_id)
    await event.delete()