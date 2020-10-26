import os
import sys
from concurrent.futures.thread import ThreadPoolExecutor

from flask import Flask, render_template, request, jsonify
from pyfladesk import init_gui
from win32api import GetSystemMetrics
import calc
import ctypes


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


if getattr(sys, 'frozen', False):
    app = Flask(__name__, template_folder=resource_path('templates'), static_folder=resource_path('static'))
else:
    app = Flask(__name__, static_url_path='/static')

executor = ThreadPoolExecutor(1)
future = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/runCalc', methods=['POST'])
def runCalc():
    global future
    result = request.form.get('calcResult', type=float)
    krouns = request.form.get('krouns', type=int)
    ExchangeRate = request.form.get('ExchangeRate', type=float)
    xApproximate = request.form.get('xApproximate', type=float)
    yApproximate = request.form.get('yApproximate', type=int)
    zApproximate = request.form.get('zApproximate', type=int)
    xincrement = request.form.get('xincrement', type=float)
    yincrement = request.form.get('yincrement', type=int)
    zincrement = request.form.get('zincrement', type=int)
    xdiviation = request.form.get('xdiviation', type=float)
    ydiviation = request.form.get('ydiviation', type=int)
    zdiviation = request.form.get('zdiviation', type=int)
    equalstolerance = request.form.get('equalstolerance', type=float)
    future = executor.submit(calc.execCalc, result, krouns, ExchangeRate,
                             xApproximate, yApproximate, zApproximate,
                             xincrement, yincrement, zincrement,
                             xdiviation, ydiviation, zdiviation, equalstolerance)
    data = {'result': 'Running'}
    return jsonify(data)


@app.route('/calcStatus', methods=['GET'])
def calcStatus():
    global future
    status = 'Nothing' if (future is None) else future.running()
    return jsonify(status=status, output=calc.output, combinations=calc.combinations, correctValues=calc.correctValues)


if __name__ == '__main__':
    # app.run(debug=True)
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    width = (GetSystemMetrics(0) * 0.8)
    height = (GetSystemMetrics(1) * 0.83)
    init_gui(app, width=width, height=height, window_title="PyFladesk", icon="static/favicon.png")
