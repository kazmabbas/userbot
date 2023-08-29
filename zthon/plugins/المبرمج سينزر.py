@zedub.tgbot.on(events.InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("يوسف") and event.query.user_id == zedub.uid:
        ZPIC = gvarstatus("ALIVE_PIC")
        buttons = [[Button.url("مطورين سورس ريفز العربي - 𝙍𝙀𝙁𝙕 𝙐𝙎𝙀𝙍𝘽𝙊𝙏", "https://t.me/def_Zoka"),],[Button.url("المطور فيجر", "https://t.me/Q_2_Q_Y"), Button.url("المطور سينزر", "https://t.me/IC_X_K"),],[Button.url("المطور رينزر¹", "https://t.me/r1e_z"),],[Button.url("المطورة سيلينا ", "https://t.me/celen0"),],[Button.url("مطـور السـورس", "https://t.me/IC_X_K"),]]
        if ZPIC and ZPIC.endswith((".jpg", ".png", "gif", "mp4")):
            result = builder.photo(ZPIC,text=Channels, buttons=buttons, link_preview=True)
        elif ZPIC and ZPIC.endswith((".gif", ".mp4")):
            result = builder.document(ZPIC,title="zedub",text=Channels,buttons=buttons,link_preview=True)
        else:
            result = builder.article(title="zedub",text=Channels,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="يوسف")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(TG_BOT, "ريفز")
    await response[0].click(event.chat_id)
    await event.delete()