# -*- coding: utf-8 -*-
"""
Create on: 2018-5-3
@Author  : sunhailin-Leo
@File    : bankend.py
"""
# Inside Package
from spider_timeline import *

# Library Package
from pyecharts_javascripthon.api import TRANSLATOR
from flask import Flask, render_template

app = Flask(__name__)
REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@app.route("/")
def render():
    _overlap = render_picture()
    return render_template('chart.html',
                           chart_id=_overlap.chart_id,
                           host=REMOTE_HOST,
                           my_width="100%",
                           my_height=600,
                           my_option=TRANSLATOR.translate(_overlap.options).as_snippet(),
                           script_list=_overlap.get_js_dependencies())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
