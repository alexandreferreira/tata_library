from werkzeug.exceptions import abort
from models.livros import Livros
from models.token import Token
from models.usuarios import Usuario
from Crypto.Hash import SHA256
from utils import JSONEncoder

__author__ = 'alexandreferreira'


def mudar_senha(params):
    pass


def mudar_email(params):
    pass


def visualizar_perfil(params):
    pass


def cadastrar_usuario(params):
    nome = params.get('nome')
    senha = params.get('senha')
    email = params.get('email')
    username = params.get('username')
    if nome and email and username:
        if not Usuario.collection().find_one({'username': username}):
            if not Usuario.collection().find_one({'email': email}):
                u = Usuario()
                u.nome = nome
                u.email = email
                u.username = username
                hash = SHA256.new()
                hash.update(senha)
                u.senha = hash.hexdigest()
                usuario_dict = Usuario.make_dict_from_usuario(u)
                Usuario.collection().insert(usuario_dict)
                return "sucesso!"
            else:
                return "email ja existe"
        else:
            return "usuario ja cadastrado"
    else:
        abort(500)


def logar(params):
    usuario = params.get('usuario')
    email = params.get('email')
    senha = params.get('senha')
    if senha and (usuario or email):
        hash = SHA256.new()
        hash.update(senha)
        query = {'senha': hash.hexdigest()}
        if usuario:
            query['username'] = usuario
        elif email:
            query['email'] = email
        else:
            abort(403)
        u_dict = Usuario.collection().find_one(query)
        u = Usuario()
        u = Usuario.make_usuario_from_dict(u, u_dict)
        if u:
            token_dict = Token.collection().find_one({'usuario': u.get_id(), 'expired': False})
            if token_dict:
                t = Token().make_from_dict(token_dict)
                return t.token
            else:
                t = Token()
                t.token = Token.generate_token()
                t.usuario = u.get_id()
                t.expired = False
                Token.collection().insert(t.make_dict())
                return t.token
        else:
            abort(403)
    else:
        abort(500)