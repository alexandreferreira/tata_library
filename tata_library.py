from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
from utils import get_params, login_required

from models.autores import Autores
from models.livros import Livros
from views import livros_view, usuario_view, autores_view


@app.route('/tste')
def hello_world():
    a = Autores()
    a.nome = 'Alexandre'
    ab = Autores()
    ab.nome = 'Siqueira'

    a._id = Autores.collection().insert(Autores.make_dict_from_autor(a))

    ab._id = Autores.collection().insert(Autores.make_dict_from_autor(ab))

    livro1 = Livros()
    livro1.nome = 'Livro 1'
    livro1.ibsn = '1'
    livro1.autor.append(a.get_id())

    livro2 = Livros()
    livro2.nome = 'Livro 2'
    livro2.autor.append(ab.get_id())
    livro2.ibsn = '2'

    livro1._id = Livros.collection().insert(Livros.make_dict_from_livro(livro1))
    a.set_livro(livro1)

    livro2._id = Livros.collection().insert(Livros.make_dict_from_livro(livro2))
    ab.set_livro(livro2)
    return 'Hello World!'


@app.route('/livros/todos/', methods=['GET', 'POST'])
def livros_todos():
    params = get_params(request)
    if request.method == 'GET':
        return livros_view.livros_todos_get(params)
    else:
        return livros_view.livros_todos_post(params)


@app.route('/livros/lidos/', methods=['GET', 'POST'])
@login_required
def livros_lidos():
    params = get_params(request)
    if request.method == 'GET':
        return livros_view.livros_lidos_get(params)
    else:
        return livros_view.livros_lidos_post(params)


@app.route('/livros/comprados/', methods=['GET', 'POST'])
@login_required
def livros_comprados():
    params = get_params(request)
    if request.method == 'GET':
        return livros_view.livros_comprados_get(params)
    else:
        return livros_view.livros_comprados_post(params)


@app.route('/livros/desejo/', methods=['GET', 'POST'])
@login_required
def livros_desejo():
    params = get_params(request)
    if request.method == 'GET':
        return livros_view.livros_desejo_get(params)
    else:
        return livros_view.livros_desejo_post(params)


@app.route('/livros/avaliacoes/', methods=['GET', 'POST'])
@login_required
def livros_avaliacoes():
    params = get_params(request)
    if request.method == 'GET':
        return livros_view.livros_avaliacoes_get(params)
    else:
        return livros_view.livros_avaliacoes_post(params)

@app.route('/livros/resenhas/', methods=['GET', 'POST'])
@login_required
def livros_resenhas():
    params = get_params(request)
    if request.method == 'GET':
        return livros_view.livros_resenhas_get(params)
    else:
        return livros_view.livros_resenhas_post(params)


@app.route('/autor/todos/', methods=['GET', 'POST'])
@login_required
def autor_todos():
    params = get_params(request)
    if request.method == 'GET':
        return autores_view.autores_todos_get(params)
    else:
        return autores_view.autores_todos_post(params)

@app.route('/autor/todos/', methods=['GET'])
@login_required
def autor_livros_todos():
    params = get_params(request)
    return autores_view.autor_livros_todos(params)


@app.route('/usuario/cadastrar/', methods=['POST'])
def cadastrar_usuario():
    params = get_params(request)
    return params
    #return usuario_view.cadastrar_usuario(params)

@app.route('/usuario/logar/', methods=['POST'])
def logar():
    params = get_params(request)
    return usuario_view.logar(params)

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
