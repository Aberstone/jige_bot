from os import path
from typing import Any

import nonebot as nb


def init(config_object: Any) -> nb.NoneBot:
    nb.init(config_object)
    bot = nb.get_bot()

    # bot.server_app.before_serving(cache.init)
    # bot.server_app.before_serving(db.init)

    nb.load_builtin_plugins()
    nb.load_plugins(path.join(path.dirname(__file__), 'plugins'),
                    'bot.plugins')

    return bot
