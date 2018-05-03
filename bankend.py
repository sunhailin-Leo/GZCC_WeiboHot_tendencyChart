# -*- coding: utf-8 -*-
"""
Create on: 2018-5-3
@Author  : sunhailin-Leo
@File    : bankend.py
"""
from spider_timeline import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def render():
    render_picture()
    return render_template('render.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
