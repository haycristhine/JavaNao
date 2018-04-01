#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/tarefa1/alomundo', methods=['POST', 'GET'])
def alomundo():
    """questao 1."""
    if request.method == 'POST':
        name = request.form['name']
        return render_template('alomundo/show_name.html', name=name)
    else:
        return render_template('alomundo/index.html')


@app.route('/tarefa1/mostraheaders')
def headers():
    headers = request.headers
    return render_template('headers.html', headers=headers)


@app.route('/tarefa1/somatorio')
def somatorio():
    try:
        start = request.args.get('inicio', type=int)
        end = request.args.get('fim', type=int)
        if not (start and end):
            raise KeyError
        if start > end:
            raise ValueError
    except KeyError:
        return render_template('error_message.html', message='São necessários os parâmetros "inicio" e "fim"')
    except ValueError:
        return render_template('error_message.html', message='Valores inválidos para início e fim!')
    sum_result = sum(range(start, end+1))
    return render_template('somatorio.html', start=start, end=end, sum_result=sum_result)


def main():
    app.run(debug=True, port=8080)


if __name__ == "__main__":
    main()
