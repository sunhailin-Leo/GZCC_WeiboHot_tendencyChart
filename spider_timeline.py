# -*- coding: utf-8 -*-
"""
Create on: 2018-5-3
@Author  : sunhailin-Leo
@File    : spider_timeline.py
"""
import time
from pyecharts import Line, Overlap


LABEL = "广州商学院 外卖"


def transfer_localtime(tm: int):
    # localtime转换成新的时间格式(2016-05-05 20:28:54)
    return time.strftime("%H:%M", time.localtime(tm))


def read_file():
    rank_list = []
    value_list = []
    time_list = []
    with open("data.txt", "r") as fp:
        for line in fp.readlines():
            line_list = line.split(",")
            rank_list.append(line_list[0])
            value_list.append(line_list[2])
            time_list.append(transfer_localtime(tm=int(int(line_list[-1]) / 1000)))
    return draw_line(attr_list=time_list, value_list=value_list, rank_list=rank_list)


def draw_line(attr_list, value_list, rank_list):
    overlap = Overlap()

    # 微博热搜量
    line = Line(title="广州商学院 外卖(微博热搜量)",
                title_text_size=20,
                subtitle=
                "Made By sunhailin-Leo (数据从21点23分开始采集) --- "
                "截止到:{}".format(time.strftime("%Y年%m月%d日 %H时%M分%S秒")),
                subtitle_text_size=14,
                subtitle_color="#A8A8A8")
    line.add("微博热搜量", attr_list, value_list,
             legend_pos="center",
             legend_top="bottom",
             mark_point=["min", "average"],
             mark_line=['min', "max", "average"],
             mark_point_symbolsize="72",
             is_more_utils=True,
             xaxis_name="时间",
             xaxis_name_pos="end",
             yaxis_name="微博热搜量(人/次)",
             yaxis_name_pos="start")

    # 微博热搜排名
    line_1 = Line()
    line_1.add("微博热搜排名", attr_list, rank_list,
               legend_pos="center",
               legend_top="bottom",
               mark_point=["max", "average"],
               mark_point_symbolsize="72",
               is_more_utils=True,
               is_yaxis_inverse=True,
               xaxis_name="时间",
               xaxis_name_pos="end",
               yaxis_name="排名位置",
               yaxis_name_pos="start")

    # 复合图
    overlap.add(line)
    overlap.add(line_1, yaxis_index=1, is_add_yaxis=True)

    return overlap


def render_picture():
    return read_file()
