import os

with open("config.py", "w", encoding="utf-8") as f:
    f.write("from nonebot.default_config import *\n\n")
    env_superusers = os.getenv("SUPERUSERS", '{447605228}')
    f.write("SUPERUSERS = %s\n" % env_superusers)
    f.write('HOST = "0.0.0.0"\n')
    env_port = os.getenv("PORT", "32080")
    f.write('PORT = %s\n' % env_port)
    f.write("COMMAND_START = {'', '/', '!', '／', '！'}\n")
    env_session_timeout = os.getenv("SESSION_RUN_TIMEOUT", "20")
    f.write("SESSION_RUN_TIMEOUT = timedelta(seconds=%s)\n\n" % env_session_timeout)
    fpd = os.getenv("REQUEST_FRIEND_COMMENT_PASSWD", "FRIEND")
    f.write('REQUEST_FRIEND_COMMENT_PASSWD = "%s"\n' % fpd)
