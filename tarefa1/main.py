#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'Super Secret Key'
app.sum_counter = 0
users = dict()


@app.route('/tarefa1/alomundo', methods=['POST', 'GET'])
def alomundo():
    """questao 1."""
    if request.method == 'POST':
        name = request.form['name']
        return render_template('alomundo/show_name.html', name=name)
    return render_template('alomundo/index.html')


@app.route('/tarefa1/mostraheaders')
def headers():
    return render_template('headers.html', headers=request.headers)


@app.route('/')
def index():
    try:
        user = session['username']
    except KeyError:
        user = None
    return render_template('index.html', user=user)


def get_session_username():
    try:
        if session['username'] and users[session['username']]:
            return session['username']
    except KeyError:
        return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if get_session_username():
            return redirect(url_for('index'))
        return render_template('login.html')

    if request.method == 'POST':
        request_username = request.form['username']
        request_password = request.form['password']

        if not users.get(request_username):
            users[request_username] = {}
            users[request_username]['password'] = request_password

        else:
            if users[request_username]['password'] != request_password:
                return render_template(
                    'error_message.html', message="Senha inválida!")

        session['username'] = request_username
        session.modified = True
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('sum_counter', None)
    session.pop('username', None)
    session.modified = True
    return redirect(url_for('index'))


@app.route('/tarefa1/somatorio')
def somatorio():
    user = get_session_username()
    kwargs = dict()
    if user:
        try:
            users[user][request.headers.get('User-Agent')] += 1
        except KeyError:
            users[user][request.headers.get('User-Agent')] = 1
        try:
            session['sum_counter'] += 1
        except KeyError:
            session['sum_counter'] = 1

        kwargs['browser_counter'] = users[user][request.headers.get(
            'User-Agent')]
        kwargs['session_counter'] = session['sum_counter']

    app.sum_counter += 1

    try:
        start = request.args.get('inicio', type=int)
        end = request.args.get('fim', type=int)
        if not (start and end):
            raise KeyError
        if start > end:
            raise ValueError
    except KeyError:
        return render_template(
            'error_message.html',
            message='São necessários os parâmetros "inicio" e "fim"')
    except ValueError:
        return render_template(
            'error_message.html',
            message='Valores inválidos para início e fim!')

    sum_result = sum(range(start, end + 1))
    return render_template(
        'somatorio.html',
        start=start,
        end=end,
        sum_result=sum_result,
        app_counter=app.sum_counter,
        **kwargs)


def main():
    app.run(debug=True, port=8080)


if __name__ == "__main__":
    main()
