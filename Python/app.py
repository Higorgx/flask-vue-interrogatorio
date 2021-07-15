from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request
import uuid

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/perguntas', methods=['GET'])
def Perguntas():
    response_object = {'status': 'sucesso'}
    response_object['questions'] = QUESTIONS
    return jsonify(response_object)

QUESTIONS = [
    {
        'id': uuid.uuid4().hex,
        'pergunta': 'a arte de enganar',
        'resposta': False
    },
    {
        'id': uuid.uuid4().hex,
        'pergunta': 'Tecnicas de Invasão',
        'resposta': False
    },
    {
        'id': uuid.uuid4().hex,
        'pergunta': 'As Armas da Persuasão',
        'resposta': False
    }
]

if __name__ == '__main__':
    app.run()