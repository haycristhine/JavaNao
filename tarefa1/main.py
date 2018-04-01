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


def main():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
