from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cursos = []
eventos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cursos')
def cursos_page():
    return render_template('cursos.html', cursos=cursos)

@app.route('/eventos')
def eventos_page():
    return render_template('eventos.html', eventos=eventos)

@app.route('/cursos/criar', methods=['POST'])
def criar_curso():
    id_novo = len(cursos) + 1
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    carga_horaria = request.form['carga_horaria']
    cursos.append((id_novo, titulo, descricao, carga_horaria))
    return redirect(url_for('cursos_page'))

@app.route('/cursos/atualizar/<int:id>', methods=['POST'])
def atualizar_curso(id):
    for curso in cursos:
        if curso[0] == id:
            curso = (id, request.form['titulo'], request.form['descricao'], request.form['carga_horaria'])
            break
    return redirect(url_for('cursos_page'))

@app.route('/cursos/deletar/<int:id>', methods=['POST'])
def deletar_curso(id):
    global cursos
    cursos = [curso for curso in cursos if curso[0] != id]
    return redirect(url_for('cursos_page'))

@app.route('/eventos/criar', methods=['POST'])
def criar_evento():
    id_novo = len(eventos) + 1
    data = request.form['data']
    descricao = request.form['descricao']
    tipo = request.form['tipo']
    eventos.append((id_novo, data, descricao, tipo))
    return redirect(url_for('eventos_page'))

@app.route('/eventos/atualizar/<int:id>', methods=['POST'])
def atualizar_evento(id):
    for evento in eventos:
        if evento[0] == id:
            evento = (id, request.form['data'], request.form['descricao'], request.form['tipo'])
            break
    return redirect(url_for('eventos_page'))

@app.route('/eventos/deletar/<int:id>', methods=['POST'])
def deletar_evento(id):
    global eventos
    eventos = [evento for evento in eventos if evento[0] != id]
    return redirect(url_for('eventos_page'))

if __name__ == '__main__':
    app.run(debug=True)