

# -*- coding: utf-8 -*-

import pandas as pd
# from shapely.geometry import Point, shape
import pandas as pd
import cx_Oracle
import numpy as np
import os
import urllib.request
import pprint
import webview


from flask import send_from_directory
from flask import Flask, flash, redirect, render_template, request, session, abort, Response
import json
import sys
import json
from pygments import highlight, lexers, formatters
import pprint
import os
import v
import dataforweb as dw
from threading import Thread



app = Flask(__name__)


@app.route('/')
def hello_world():
    data = dw.pulldata()
    return render_template("index.html", data=data)



def start_server():
    app.run()
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.route('/')
# def home():
#     if not session.get('logged_in'):
#         return render_template('login.html')
#     else:
#         return "Hello Boss!"
@app.route("/graphs")
def index():
    return render_template("index.html")

@app.route("/options")
def options():
    return render_template("options.html")


@app.route("/data")
def data():
        data = dw.pulldata()
        return data



if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
    t = Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window("test", "http://localhost:5000/")

    sys.exit()