from bson.objectid import ObjectId
import pymongo
from werkzeug.exceptions import abort
from models.autores import Autores
from utils import JSONEncoder

__author__ = 'alexandreferreira'


def autores_todos_get(params):
    autores = Autores.collection().find({}).sort([('nome', pymongo.ASCENDING)])
    livros_list = []
    for autor in autores:
        livros_list.append(autor)
    return JSONEncoder().encode(livros_list)


def autor_livros_todos(params):
    autor = Autores.collection().find_one({'_id': ObjectId(params.get('autor'))})
    if autor:
        autor = Autores.make_autor_from_dict(Autores(), autor)
        return JSONEncoder().encode(autor.get_livros())
    else:
        abort(500)


def autores_todos_post(params):
    nome = params.get('nome')
    if nome:
        autor = Autores()
        autor.nome = nome
        autor_dict = Autores.make_dict_from_autor(autor)
        Autores.collection().insert(autor_dict)
    else:
        abort(500)