import random

from nonebot import CommandSession, MessageSegment

from bot.aio import requests
from . import cg

CHP_API = "https://chp.shadiao.app/api.php"


@cg.command("chp", aliases=("鸡哥牛逼", "鸡哥霸气", "鸡哥强"), only_to_me=False)
async def chp(session: CommandSession):
    await session.send(MessageSegment.text(await fang_chp()))


async def fang_chp():
    chp_for_chicken = ""
    chp_content = (await (await requests.get(url=CHP_API)).content).decode()
    if "你" in chp_content:
        chp_for_chicken = chp_content.replace("你", random.choice(("鸡哥", "阿鸡", "钵钵鸡")))
    return chp_for_chicken or "暂时放不出彩虹屁来了"
