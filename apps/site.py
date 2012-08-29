# -*- coding: utf-8 -*-

"""
    Site app
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from flask import Blueprint, render_template


######################################################
###
### App
###
######################################################

app = Blueprint('site', __name__)


######################################################
###
### Routes
###
######################################################

@app.route('/')
def index():
    return render_template('site/index.html')
