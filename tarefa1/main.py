#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/tarefa1/alomundo', methods=['POST', 'GET'])
def alomundo():
    """questao 1."""
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        return render_template('alomundo/show_name.html', name=name)
    else:
        return render_template('alomundo/index.html')


def main():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
