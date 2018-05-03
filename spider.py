# -*- coding: utf-8 -*-
"""
Create on: 2018-5-3
@Author  : sunhailin-Leo
@File    : spider.py
"""
import json
import time
import requests
from lxml import etree

Url = "http://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6"


def parse_page():
    resp = requests.get(Url, headers={"User-Agent": ""})
    txt_content = resp.content.decode("UTF-8")
    for line in txt_content.splitlines():
        if line.startswith(
                '<script>STK && STK.pageletM && STK.pageletM.view({"pid":"pl_top_realtimehot"') and line.endswith(
                '</script>'):
            line = line.replace("<script>STK && STK.pageletM && STK.pageletM.view(", "").replace(")</script>", "")
            json_res = json.loads(line)
            return json_res['html']


def parse_page_table(code):
    element = etree.HTML(code)
    for tr in element.xpath('//div[@class="hot_ranklist"]/table/tr'):
        rank = tr.xpath('string(td[@class="td_01"]/span/em)')
        name = tr.xpath('string(td[@class="td_02"]/div/p/a)')
        count = tr.xpath('string(td[@class="td_03"]/p/span)')
        if "广州商学院" in name:
            format_str = "{},{},{},{}\n".format(rank, name, count, str(int(time.time() * 1000)))
            print(format_str)
            with open('data.txt', 'a') as fp:
                fp.write(format_str)


def spider():
    res = parse_page()
    parse_page_table(res)


if __name__ == '__main__':
    print("Start time: {}".format(time.time()))
    while True:
        spider()
        time.sleep(2)

