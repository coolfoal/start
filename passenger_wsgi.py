# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:24:36 2023

@author: coolfoal
"""

from bottle import route, run, template, default_app
from time import ctime


@route('/')
def index():
    return template('<b>Time: {{thetime}}</b>!', thetime=ctime())

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)


if __name__ == '__main__':
    run(host='localhost', port=8080)
else:
    application = default_app()