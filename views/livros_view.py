import json
from flask import abort
import pymongo
from models.autores import Autores
from models.livros import Livros
from models.usuarios import Usuario
from utils import JSONEncoder, save_file
from bson.objectid import ObjectId
import utils

__author__ = 'alexandreferreira'


def livros_todos_get(params):
    livros = Livros.collection().find({}).sort([('titulo', pymongo.ASCENDING)])
    livros_list = []
    for livro in livros:
        livros_list.append(livro)
    return JSONEncoder().encode(livros_list)


def livros_todos_post(params):
    if params.get('post_file') and params.get('post_file').get('image'):
        autor = Autores.collection().find_one({'_id': ObjectId(params.get('autor'))})
        if autor:
            livro = Livros()
            livro.image = save_file(params.get('post_file').get('image'))
            livro.nome = params.get('nome')
            livro.ibsn = params.get('ibsn')
            livro.autor.append(params.get('autor'))
            livro_dict = Livros.make_dict_from_livro(livro, None)
            livro._id = Livros.collection().insert(livro_dict)
            autor = Autores.make_autor_from_dict(Autores(), autor)
            autor.set_livro(livro)
            return "OK"
        else:
            abort(500)

    else:
        abort(500)


def livros_lidos_get(params):
    usuario = Usuario()
    Usuario.make_usuario_from_dict(usuario, Usuario.collection().find_one({'_id': ObjectId(params.get('usuario'))}))
    livros = Livros.make_dict_from_livro(None, usuario.get_livros_lidos(), many=True)
    return JSONEncoder().encode(livros)


def livros_lidos_post(params):
    usuario = Usuario.collection().find_one({'_id': ObjectId(params.get('usuario'))})
    livro = Livros.collection().find_one({'_id': ObjectId(params.get('livro'))})
    if usuario and livro:
        usuario = Usuario.make_usuario_from_dict(Usuario(), usuario)
        livro = Livros.make_livro_from_dict(Livros(), livro)
        usuario.set_livro_lido(livro)
        return "ok"
    else:
        abort(500)


def livros_comprados_get(params):
    usuario = Usuario()
    Usuario.make_usuario_from_dict(usuario, Usuario.collection().find_one())
    livros = Livros.make_dict_from_livro(None, usuario.get_livros_comprados(), many=True)
    return JSONEncoder().encode(livros)


def livros_comprados_post(params):
    usuario = Usuario.collection().find_one({'_id': ObjectId(params.get('usuario'))})
    livro = Livros.collection().find_one({'_id': ObjectId(params.get('livro'))})
    if usuario and livro:
        usuario = Usuario.make_usuario_from_dict(Usuario(), usuario)
        livro = Livros.make_livro_from_dict(Livros(), livro)
        usuario.set_livro_comprado(livro)
        return "ok"
    else:
        abort(500)


def livros_desejo_get(params):
    usuario = Usuario()
    Usuario.make_usuario_from_dict(usuario, Usuario.collection().find_one())
    livros = Livros.make_dict_from_livro(None, usuario.get_livros_desejo(), many=True)
    return JSONEncoder().encode(livros)


def livros_desejo_post(params):
    usuario = Usuario.collection().find_one({'_id': ObjectId(params.get('usuario'))})
    livro = Livros.collection().find_one({'_id': ObjectId(params.get('livro'))})
    if usuario and livro:
        usuario = Usuario.make_usuario_from_dict(Usuario(), usuario)
        livro = Livros.make_livro_from_dict(Livros(), livro)
        usuario.set_livro_deseja(livro)
        return "ok"
    else:
        abort(500)


def livros_avaliacoes_get(params):
    usuario = Usuario()
    Usuario.make_usuario_from_dict(usuario, Usuario.collection().find_one())
    avaliacoes = usuario.get_livros_avaliados()
    return JSONEncoder().encode(avaliacoes)


def livros_avaliacoes_post(params):
    usuario = Usuario.collection().find_one({'_id': ObjectId(params.get('usuario'))})
    livro = Livros.collection().find_one({'_id': ObjectId(params.get('livro'))})
    avaliacao = int(params.get('avaliacao'))
    if usuario and livro and (0 <= avaliacao <= 5):
        usuario = Usuario.make_usuario_from_dict(Usuario(), usuario)
        livro = Livros.make_livro_from_dict(Livros(), livro)
        usuario.set_avaliacao(avaliacao, livro)
        return "ok"
    else:
        abort(500)


def livros_resenhas_get(params):
    usuario = Usuario()
    Usuario.make_usuario_from_dict(usuario, Usuario.collection().find_one())
    resenhas = usuario.get_livros_resenhados()
    return JSONEncoder().encode(resenhas)


def livros_resenhas_post(params):
    usuario = Usuario.collection().find_one({'_id': ObjectId(params.get('usuario'))})
    livro = Livros.collection().find_one({'_id': ObjectId(params.get('livro'))})
    resenha = params.get('avaliacao')
    if usuario and livro and resenha:
        usuario = Usuario.make_usuario_from_dict(Usuario(), usuario)
        livro = Livros.make_livro_from_dict(Livros(), livro)
        usuario.set_resenha(resenha, livro)
        return "ok"
    else:
        abort(500)