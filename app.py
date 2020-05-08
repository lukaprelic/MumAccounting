from flask import Flask, render_template, request, jsonify

import calc

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/runCalc', methods=['POST'])
def hello():
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
    output = calc.execCalc(result, krouns, xExchangeRate,
                  yApproximate, zApproximate,
                  xincrement, yincrement, zincrement,
                  xdiviation, ydiviation, zdiviation)
    data = {'result': output}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
