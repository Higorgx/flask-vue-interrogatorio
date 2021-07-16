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

@app.route('/result', methods=['GET'])
def get_result():
    response_object = {'status': 'success'}
    response_object['result'] = RESULTS
    return jsonify(response_object)

@app.route('/result', methods=['POST'])
def set_result():
    post_data = request.get_json()
    answers = post_data['answers']
    print(answers)

    yesAnswers = answers.count('sim')

    if yesAnswers == 0:
        result = 'Inocente'

    if yesAnswers == 2:
        result = 'Suspeito'
    
    if yesAnswers >= 3 and yesAnswers <= 4:
        result = 'Cúmplice'

    if yesAnswers == 5:
        result = 'Assassino'

    response_object = {'result': result}
    return jsonify(response_object)

@app.route('/perguntas/<int:id>', methods=['GET'])
def get_book_by_id(id):
    return_value = QUESTIONS.get_Perguntas(id)
    return jsonify(return_value)

# sanity check route
@app.route('/perguntas', methods=['GET'])
def get_Perguntas():
    response_object = {'status': 'sucesso'}
    response_object['questions'] = QUESTIONS
    return jsonify(response_object)

RESULTS = []

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