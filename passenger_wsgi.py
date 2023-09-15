# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:24:36 2023

@author: coolfoal
"""

from bottle import route, run, template, default_app
from time import ctime


@route('/')
def index(name):
    return template('<b>Time: {{thetime}}</b>!', thetime=ctime()))

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

#run(host='localhost', port=8080)
application = default_app()