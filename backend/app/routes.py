# -*- coding: utf-8 -*-
import json

from app import app
from flask import jsonify, request
from werkzeug.exceptions import NotFound

books_list = [
    {'id': 1, 'name': 'Приключения копетана Блата', 'author': 'Рафаэль Саботини',
     'description': 'Клёвая книга про ператоф'},
    {'id': 2, 'name': 'Последний из могекан', 'author': 'Фенимор Купер', 'description': 'Интересная книга'},
    {'id': 3, 'name': 'Грабители морей', 'author': 'Луи Жаколио',
     'description': 'Не менее клёвая книга про ператоф'},
    {'id': 4, 'name': 'Пожиратели огня', 'author': 'Луи Жаколио', 'description': 'Австралия, ура!'},
]

id = len(books_list) + 1


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Мир!"


@app.route('/books', methods=['GET', 'POST'])
def books():
    global books_list
    global id
    if request.method == 'GET':
        return jsonify(books_list), 200
    elif request.method == 'POST':
        req = json.loads(request.data, strict=False)
        print(req)
        book = {}
        try:
            book['id'] = id
            book['name'] = req['name']
            book['author'] = req['author']
            book['description'] = req['description']
        except KeyError as e:
            print('Exception!', e)
        books_list.append(book)
        id += 1
        print(books_list)
        print('id', id)
        return '{}', 200


@app.route('/books/<int:num_id>', methods=['GET', 'PUT', 'DELETE'])
def book(num_id):
    global books_list
    if request.method == 'GET':
        res = list(filter(lambda x: x['id'] == num_id, books_list))
        if len(res) == 1:
            return jsonify(res[0])
        else:
            return app.make_response(app.handle_user_exception(NotFound()))
    elif request.method == 'DELETE':
        books_list = list(filter(lambda x: x['id'] != num_id, books_list))
        return '{}', 200
