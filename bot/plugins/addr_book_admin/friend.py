from nonebot import on_request, RequestSession, get_bot

bot = get_bot()


@on_request("friend")
async def _(session: RequestSession):
    if session.event.comment == bot.config.REQUEST_FRIEDN_COMMENT_PASSWD:
        if session.event.user_id in bot.config.SUPERUSERS:
            await session.approve("Admin_" + str(session.event.user_id))
        else:
            await session.approve(str(session.event.user_id))
    else:
        await session.reject("口令错误，你不是鸡哥的信徒！！")
