FROM python:3.8-slim
LABEL author="aberstone"

#print()时在控制台正常显示中文
ENV PYTHONIOENCODING=utf-8

RUN cat /etc/apt/sources.list

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list

# 设置系统时间与时区
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone

# 代码复制过来后的路径
RUN mkdir /etc/bot_src

ADD ./. /etc/bot_src

WORKDIR /etc/bot_src

RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r /etc/bot_src/requirements.txt
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ hypercorn

#
#RUN python3 main.py
CMD ["hypercorn","main:app","-b","0.0.0.0:32080"]
