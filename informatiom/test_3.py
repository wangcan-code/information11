# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello python'


if __name__ == '__main__':
    app.run(debug=True)
