from concurrent.futures.thread import ThreadPoolExecutor

from flask import Flask, render_template, request, jsonify
from pyfladesk import init_gui
from win32api import GetSystemMetrics
import calc
import ctypes

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
    xExchangeRate = request.form.get('xExchangeRate', type=float)
    yApproximate = request.form.get('yApproximate', type=int)
    zApproximate = request.form.get('zApproximate', type=int)
    xincrement = request.form.get('xincrement', type=float)
    yincrement = request.form.get('yincrement', type=int)
    zincrement = request.form.get('zincrement', type=int)
    xdiviation = request.form.get('xdiviation', type=float)
    ydiviation = request.form.get('ydiviation', type=int)
    zdiviation = request.form.get('zdiviation', type=int)
    future = executor.submit(calc.execCalc, result, krouns, xExchangeRate,
                             yApproximate, zApproximate,
                             xincrement, yincrement, zincrement,
                             xdiviation, ydiviation, zdiviation)
    # output = calc.execCalc(result, krouns, xExchangeRate,
    #                      yApproximate, zApproximate,
    #                      xincrement, yincrement, zincrement,
    #                      xdiviation, ydiviation, zdiviation)
    data = {'result': 'Running'}
    return jsonify(data)


@app.route('/calcStatus', methods=['GET'])
def calcStatus():
    global future
    status = 'Nothing' if (future is None) else future.running()

    return jsonify(status=status,output=calc.output,combinations=calc.combinations,correctValuesCount=len(calc.correctValues))


if __name__ == '__main__':
    app.run(debug=True)
# ctypes.windll.shcore.SetProcessDpiAwareness(2)
# width = (GetSystemMetrics(0) * 0.8)
# height = (GetSystemMetrics(1) * 0.8)
# init_gui(app, width=width, height=height, window_title="PyFladesk", icon="appicon.png")
#
