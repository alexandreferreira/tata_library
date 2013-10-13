
import utils

__author__ = 'alexandreferreira'

class Autores (object):

    def __init__(self):
        self._id = None
        self.livros = []
        self.nome = None

    def get_id(self):
        return self._id

    @staticmethod
    def make_dict_from_autor(self):
        autor_dict = {}
        if self._id:
            autor_dict['_id'] = self._id
        if self.nome:
            autor_dict['nome'] = self.nome
        if self.livros:
            autor_dict['livros'] = self.livros
        return autor_dict

    @staticmethod
    def make_autor_from_dict (self, autor_dict):
        if autor_dict.get('_id'):
            self._id = autor_dict.get('_id')
        if autor_dict.get('nome'):
            self.nome = autor_dict.get('nome')
        if autor_dict.get('livros'):
            self.livros = autor_dict.get('livros')
        return self

    @staticmethod
    def collection():
        db = utils.connect_mongo()
        return db.autores

    def get_livros(self):
        from models.livros import Livros
        query = {'_id': {'$in': self.livros}}
        livros_list = []
        livros = Livros.collection().find(query)
        for livro in livros:
            l = Livros()
            Livros.make_livro_from_dict(l, livro)
            livros_list.append(l)
        return livros_list

    def set_livro(self, livro):
        self.livros.append(livro.get_id())
        self.collection().update({'_id': self._id}, {'$push': {'livros': livro.get_id()}})
        return self




