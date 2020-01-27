from flask import Flask, jsonify, request
app = Flask(__name__)
database = dict()
database['ALUNO'] = []
database['PROFESSOR'] = []
@app.route('/')

def all():
    return jsonify(database)

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

#insere aluno
@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

#procura aluno por ID
@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return '', 404

#insere professor
@app.route('/professores', methods=['POST'])
def novo_professor():
    novo_professor = request.get_json()
    database['PROFESSOR'].append(novo_professor)
    return jsonify(database['PROFESSOR'])

#Procura professor
@app.route('/professores/<int:id_professor>', methods=['GET'])
def localiza_professor(id_professor):
    for professor in database['PROFESSOR']:
        if professor ['id'] == id_professor:
            return jsonify(professor)
    return '', 404

#deleta aluno
@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def remove_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            return jsonify(database['ALUNO'])
    return 'aluno não encontrado', 404

#deleta professor
@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def remove_professor(id_professor):
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            database['PROFESSOR'].remove(professor)
            return jsonify(database['PROFESSOR'])
    return 'professor não encontrado', 404

@app.route('/professores/<int:id_professor>', methods=['PUT'])
def att_professor(id_professor):
    
    dado_professor = request.get_json()
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            professor['id'] = dado_professor['id']
            professor['nome'] = dado_professor['nome']
            return jsonify(database['PROFESSOR'])

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def att_aluno(id_aluno):
    
    dado_aluno = request.get_json()
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            aluno['id'] = dado_aluno['id']
            aluno['nome'] = dado_aluno['nome']
            return jsonify(database['ALUNO'])

if __name__ == '__main__':
    app.run(host='localhost', port=5555)