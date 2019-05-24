# -*- coding: utf-8 -*-
import json

from app import app, db
from flask import jsonify, request
from werkzeug.exceptions import NotFound

from app.models import BookItem

books_list = [
    {'id': 1, 'name': 'Приключения копетана Блата', 'author': 'Рафаэль Саботини',
     'description': 'Клёвая книга про ператоф'},
    {'id': 2, 'name': 'Последний из могекан', 'author': 'Фенимор Купер', 'description': 'Интересная книга'},
    {'id': 3, 'name': 'Грабители морей', 'author': 'Луи Жаколио',
     'description': 'Не менее клёвая книга про ператоф'},
    {'id': 4, 'name': 'Пожиратели огня', 'author': 'Луи Жаколио', 'description': 'Австралия, ура!'},
]

id = len(books_list) + 2


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Мир!"


@app.route('/books', methods=['GET', 'POST'])
def books():
    global books_list
    global id
    if request.method == 'GET':
        res = get_books()
        print(res)
        return jsonify(res), 200
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
        book_item = BookItem(name=req['name'], author=req['author'], description=req['description'])
        db.session.add(book_item)
        db.session.commit()
        books_list.append(book)
        id += 1
        print(books_list)
        print('id', id)
        return '{}', 200


@app.route('/books/<int:num_id>', methods=['GET', 'PUT', 'DELETE'])
def book(num_id):
    global books_list
    if request.method == 'GET':
        res = get_book(num_id)
        if res:
            return jsonify(res), 200
        else:
            app.make_response(app.handle_user_exception(NotFound()))
    elif request.method == 'DELETE':
        book_to_delete = BookItem.query.filter_by(id=num_id).first()
        db.session.delete(book_to_delete)
        db.session.commit()
        # books_list = list(filter(lambda x: x['id'] != num_id, books_list))
        return '{}', 200
    elif request.method == 'PUT':
        req = json.loads(request.data, strict=False)
        print(req, num_id)
        updated_book = {
            'name': req['name'],
            'author': req['author'],
            'description': req['description']
        }
        upd_book = BookItem.query.filter_by(id=num_id).update(updated_book)
        # upd_book = BookItem.query.filter_by(id=num_id).first()
        print('OLOLOL', upd_book)
        db.session.commit()
        return '{}', 200


def get_books():
    books = BookItem.query.all()
    res = []
    for book in books:
        b_item = dict(book.__dict__)
        del b_item['_sa_instance_state']
        res.append(b_item)
    return res


def get_book(id):
    book = BookItem.query.filter_by(id=id).first_or_404()
    b_item = dict(book.__dict__)
    del b_item['_sa_instance_state']
    return b_item
