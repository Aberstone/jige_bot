import random
import re
from traceback import print_exc

try:
    import ujson as json
except:
    import json
from nonebot import CommandSession, MessageSegment

from bot.aio import requests
from . import cg

IMG_URL = "https://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word=鸡+表情包"
HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}


@cg.command("find", aliases=("找鸡图", "看鸡图", "鸡哥英姿"), only_to_me=False)
async def find(session: CommandSession):
    img = await crawler()
    if img.startswith("http"):
        message = str(MessageSegment.image(img))
        print(message)
        await session.send(message)
    else:
        await session.send(img)


async def crawler():
    async_response = await requests.get(url=IMG_URL, headers=HEADERS)
    img = ""
    try:
        html = (await async_response.content).decode("utf-8")
        # print(html)
        img_list = re.search("""'imgData',.*?\{.*?"data":.*?(\[.*\].*?\{\}\])\}.*?\);""", html, re.DOTALL).group(1)
        imgs = re.findall('''"objURL":.*?"(.*?)",''', img_list, re.DOTALL)
        if imgs:
            img = random.choice(imgs)
    except Exception as e:
        print_exc()
    return img or "暂时没有鸡图了"
