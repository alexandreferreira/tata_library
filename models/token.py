from models.usuarios import Usuario
import utils

__author__ = 'alexandreferreira'

from Crypto import Random


class Token:
    def __init__(self):
        self._id = None
        self.token = None
        self.usuario = None
        self.expired = False

    @staticmethod
    def generate_token():
        rndfile = Random.new()
        return rndfile.read(40).encode("hex")

    def expired_token(self):
        self.expired = True

    @staticmethod
    def get_usuario_from_token(token):
        usuario_dict = Token.collection().find_one({'token': token})
        if usuario_dict:
            usuario = Usuario()
            usuario = Usuario.make_usuario_from_dict(usuario, usuario_dict)
            return usuario
        else:
            return None

    @staticmethod
    def validate_token(token):
        if token:
            u = Token.collection().find_one({'token': token})
            if u:
                return True
            else:
                return False
        else:
            return False

    def make_dict(self):
        token_dict = {}
        if self._id:
            token_dict['_id'] = self._id
        if self.token:
            token_dict['token'] = self.token
        if self.usuario:
            token_dict['usuario'] = self.usuario
        if self.expired:
            token_dict['expired'] = self.expired
        return token_dict

    def make_from_dict(self, token_dict):
        if token_dict.get('_id'):
            self._id = token_dict.get('_id')
        if token_dict.get('token'):
            self.token = token_dict.get('token')
        if token_dict.get('usuario'):
            self.usuario = token_dict.get('usuario')
        if token_dict.get('expired'):
            self.expired = token_dict.get('expired')
        return self

    @staticmethod
    def collection():
        db = utils.connect_mongo()
        return db.tokens
