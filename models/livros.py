from models.autores import Autores

import utils

__author__ = 'alexandreferreira'


class Livros:

    def __init__(self):
        self._id = None
        self.nome = None
        self.ibsn = None
        self.image = None
        self.autor = []

    def get_id(self):
        return self._id

    @staticmethod
    def make_dict_from_livro(self, livro_dict, many=False):
        if many:
            livros = []
            for livro in livro_dict:
                livro_dict = {}
                if livro._id:
                    livro_dict['_id'] = livro._id
                if livro.nome:
                    livro_dict['nome'] = livro.nome
                if livro.ibsn:
                    livro_dict['ibsn'] = livro.ibsn
                if livro.autor:
                    livro_dict['autor'] = livro.autor
                if livro.image:
                    livro_dict['image'] = livro.image
                livros.append(livro_dict)
            return livros
        else:
            livro_dict = {}
            if self._id:
                livro_dict['_id'] = self._id
            if self.nome:
                livro_dict['nome'] = self.nome
            if self.ibsn:
                livro_dict['ibsn'] = self.ibsn
            if self.autor:
                livro_dict['autor'] = self.autor
            if self.image:
                    livro_dict['image'] = self.image
            return livro_dict

    @staticmethod
    def make_livro_from_dict(self, livro_dict, many=False):
        if many:
            livros = []
            for l in livro_dict:
                li = Livros()
                if l.get('_id'):
                    li._id = livro_dict.get('_id')
                if l.get('nome'):
                    li.nome = livro_dict.get('nome')
                if l.get('ibsn'):
                    li.ibsn = livro_dict.get('ibsn')
                if l.get('autor'):
                    li.autor = livro_dict.get('autor')
                if l.get('image'):
                    li.image = livro_dict.get('image')
                livros.append(li)
            return livros
        else:
            if livro_dict.get('_id'):
                self._id = livro_dict.get('_id')
            if livro_dict.get('nome'):
                self.nome = livro_dict.get('nome')
            if livro_dict.get('ibsn'):
                self.ibsn = livro_dict.get('ibsn')
            if livro_dict.get('autor'):
                self.autor = livro_dict.get('autor')
            if livro_dict.get('image'):
                    self.image = livro_dict.get('image')
            return self

    @staticmethod
    def collection():
        db = utils.connect_mongo()
        return db.livros

    def get_autores(self):
        query = {'_id': {'$in': self.autor}}
        autores = []
        for autor in Autores.collection().find(query):
            a = Autores()
            autores.append(Autores.make_autor_from_dict(a, autor))
        return autores

    def get_resenhas(self):
        from models.usuarios import Usuario
        query = {'resenhas.livro_id': self._id}, {'resenhas'}
        resenhas_list = []
        resenhas = Usuario.collection().find(query)
        for resenha in resenhas:
            resenhas_list.append({resenha})
        return resenhas_list

    def get_avaliacoes(self):
        from models.usuarios import Usuario
        query = {'avalicoes.livro_id': self._id}, {'avaliacoes'}
        avaliacoes_list = []
        avaliacoes = Usuario.collection().find(query)
        for avaliacao in avaliacoes:
            avaliacoes_list.append({avaliacao})






