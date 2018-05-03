# -*- coding: utf-8 -*-
"""
Create on: 2018-5-3
@Author  : sunhailin-Leo
@File    : spider_timeline.py
"""
import time
from pyecharts import Line


LABEL = "广州商学院 外卖"


def transfer_localtime(tm: int):
    # 转换成localtime
    time_local = time.localtime(tm)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%H:%M", time_local)
    return dt


def read_file():
    value_list = []
    time_list = []
    with open("data.txt", "r") as fp:
        for line in fp.readlines():
            line_list = line.split(",")
            value_list.append(line_list[2])
            time_list.append(transfer_localtime(tm=int(int(line_list[-1]) / 1000)))
    draw_line(attr_list=time_list, value_list=value_list)


def draw_line(attr_list, value_list):
    line = Line(page_title="Made By Leo",
                title="广州商学院 外卖(微博热搜量)",
                subtitle="Made By sunhailin-Leo (数据从21点23分开始采集)",
                width=1440,
                height=600)
    line.add("微博热搜量", attr_list, value_list,
             legend_pos="right",
             mark_point=["average"],
             mark_point_symbolsize="75",
             is_more_utils=True)
    line.render(path="templates/render.html")


def render_picture():
    read_file()


# if __name__ == '__main__':
#     render_picture()
