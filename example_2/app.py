# coding: utf-8

from flask import Flask, jsonify, request


app = Flask(__name__)


def _values_to_int(values):
    return map(int, values)


@app.route('/', methods=('GET', ))
def home():
    return jsonify(
        {'message': 'Valid operations: sum, subtraction'}
    )


@app.route('/sum', methods=('GET', ))
def sum():
    a, b = _values_to_int(request.args.values())
    return jsonify({
        'result': a + b
    })


@app.route('/subtraction', methods=('GET', ))
def subtraction():
    a, b = _values_to_int(request.args.values())
    return jsonify({
        'result': a - b
    })


if __name__ == '__main__':
    app.run(debug=True)
