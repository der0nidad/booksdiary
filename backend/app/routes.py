# -*- coding: utf-8 -*-
from app import app
from flask import jsonify


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Мир!"


@app.route('/books', methods=['GET'])
def books():
    books = [
        {'id': 1, 'name': 'Приключения копетана Блата', 'author': 'Рафаэль Саботини',
         'description': 'Клёвая книга про ператоф'},
        {'id': 2, 'name': 'Последний из могекан', 'author': 'Фенимор Купер', 'description': 'Интересная книга'},
        {'id': 3, 'name': 'Грабители морей', 'author': 'Луи Жаколио',
         'description': 'Не менее клёвая книга про ператоф'},
        {'id': 4, 'name': 'Пожиратели огня', 'author': 'Луи Жаколио', 'description': 'Австралия, ура!'},
    ]
    return jsonify(books)
