# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:24:36 2023

@author: coolfoal
"""

from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

#run(host='localhost', port=8080)
application = bottle.default_app()