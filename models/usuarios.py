from models.livros import Livros
import utils

__author__ = 'alexandreferreira'


class Usuario (object):

    def __init__(self):
        self._id = None
        self.username = None
        self.nome = None
        self.email = None
        self.senha = None
        self.livros_lidos = []
        self.livros_comprados = []
        self.livros_desejo = []
        self.resenhas = []
        self.avaliacoes = []

    def get_id(self):
        return self._id

    def save(self):
        if self._id:
            Usuario.collection().insert()
        else:
            pass

    def get_id_livros_avaliados(self):
        ids = []
        for avaliacao in self.avaliacoes:
            if avaliacao.get('livro_id'):
                ids.append(avaliacao.get('livro_id'))
        return ids

    def get_id_livros_resenhados(self):
        ids = []
        for resenha in self.resenhas:
            if resenha.get('livro_id'):
                ids.append(resenha.get('livro_id'))
        return ids

    @staticmethod
    def collection():
        db = utils.connect_mongo()
        return db.usuarios

    def make_dict_from_usuario(self):
        usuario_dict = {}
        if self._id:
            usuario_dict['_id'] = self._id
        if self.username:
            usuario_dict['username'] = self.username
        if self.nome:
            usuario_dict['nome'] = self.nome
        if self.email:
            usuario_dict['email'] = self.email
        if self.senha:
            usuario_dict['senha'] = self.senha
        if self.livros_lidos:
            usuario_dict['livros_lidos'] = self.livros_lidos
        if self.livros_comprados:
            usuario_dict['livros_comprados'] = self.livros_comprados
        if self.livros_desejo:
            usuario_dict['livros_desejo'] = self.livros_desejo
        if self.resenhas:
            usuario_dict['resenhas'] = self.resenhas
        if self.avaliacoes:
            usuario_dict['avaliacoes'] = self.avaliacoes
        return usuario_dict

    def make_usuario_from_dict(self, usuario_dict):

        if usuario_dict.get('_id'):
            self._id = usuario_dict.get('_id')
        if usuario_dict.get('username'):
            self.username = usuario_dict.get('username')
        if usuario_dict.get('nome'):
            self.nome = usuario_dict.get('nome')
        if usuario_dict.get('email'):
            self.email = usuario_dict.get('email')
        if usuario_dict.get('senha'):
            self.senha = usuario_dict.get('senha')
        if usuario_dict.get('livros_lidos'):
            self.livros_lidos = usuario_dict.get('livros_lidos')
        if usuario_dict.get('livros_comprados'):
            self.livros_comprados = usuario_dict.get('livros_comprados')
        if usuario_dict.get('livros_desejo'):
            self.livros_desejo = usuario_dict.get('livros_desejo')
        if usuario_dict.get('resenhas'):
            self.resenhas = usuario_dict.get('resenhas')
        if usuario_dict.get('avaliacoes'):
            self.avaliacoes = usuario_dict.get('avaliacoes')
        return self

    def get_livros_lidos(self):
        query = {'_id': {'$in': self.livros_lidos}}
        livros_list = []
        livros = Livros.collection().find(query)
        for livro in livros:
            l = Livros()
            Livros.make_livro_from_dict(l, livro)
            livros_list.append(l)
        return livros_list

    def get_livros_comprados(self):
        query = {'_id': {'$in': self.livros_comprados}}
        livros_list = []
        livros = Livros.collection().find(query)
        for livro in livros:
            l = Livros()
            Livros.make_livro_from_dict(l, livro)
            livros_list.append(l)
        return livros_list

    def get_livros_desejo(self):
        query = {'_id': {'$in': self.livros_desejo}}
        livros_list = []
        livros = Livros.collection().find(query)
        for livro in livros:
            l = Livros()
            Livros.make_livro_from_dict(l, livro)
            livros_list.append(l)
        return livros_list

    def get_livros_avaliados(self):
        avaliacoes_list = []
        for avaliacoes in self.avaliacoes:
            query = {'_id': avaliacoes.get('livro_id')}
            livro_dic = Livros.collection().find_one(query)
            avaliacoes['livro_info'] = livro_dic
            avaliacoes_list.append(avaliacoes)
        return avaliacoes_list

    def get_livros_resenhados(self):
        resenhas_list = []
        for resenha in self.resenhas:
            query = {'_id': resenha.get('livro_id')}
            livro_dic = Livros.collection().find_one(query)
            resenha['livro_info'] = livro_dic
            resenhas_list.append(resenha)
        return resenhas_list

    def set_resenha(self, resenha, livro):
        resenha_info = {'livro_id': livro.get_id(), 'resenha': resenha}
        self.resenhas.append(resenha_info)
        self.collection().update({'_id': self._id}, {'$push': {'resenhas': resenha_info}})
        return resenha_info

    def set_avaliacao(self, avaliacao, livro):
        avaliacao_info = {'livro_id': livro.get_id(), 'avaliacao': avaliacao}
        self.avaliacoes.append(avaliacao_info)
        self.collection().update({'_id': self._id}, {'$push': {'avaliacoes': avaliacao_info}})
        return avaliacao_info

    def set_livro_lido(self, livro):
        self.livros_lidos.append(livro.get_id())
        self.collection().update({'_id': self._id}, {'$push': {'livros_lidos': livro.get_id()}})
        return self

    def set_livro_comprado(self, livro):
        self.livros_comprados.append(livro.get_id())
        self.collection().update({'_id': self._id}, {'$push': {'livros_comprados': livro.get_id()}})
        return self

    def set_livro_deseja(self, livro):
        self.livros_desejo.addend(livro.get_id())
        self.collection().update({'_id': self._id}, {'$push': {'livros_desejo': livro.get_id()}})
        return self