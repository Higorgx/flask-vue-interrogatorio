from logging import DEBUG
from flask import Flask, jsonify
from flask_cors import CORS

#Configuração
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/murder', methods=['GET'])
def perguntar():
    return jsonify({
        'status': 'success',
        'questions': QUESTIONS
    })

@app.route('/murder', methods=['POST'])
def responder():        
    post_data = request.get_json()
    QUESTIONS.append({
        'answer': post_data.get('answer')
    })
    response_object['message'] = 'Respostas computadas'
    return (response_object)

QUESTIONS = [
    {
        'question': 'Telefonou para a vitima?',
        'answer': False
    },
    {
        'question': 'Esteve no local do crime?',
        'answer': False
    },
    {
        'question': 'Mora perto do local do crime?',
        'answer': False
    },
    {
        'question': 'Devia para a vitima?',
        'answer': False
    },
    {
        'question': 'Já trabalhou com a vítima?',
        'answer': False
    }
]

if __name__ == '__main__':
    app.run()
