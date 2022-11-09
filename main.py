from flask import Flask, jsonify, request
from db import *

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/gcteste', methods=['POST', 'GET'])
def gc_teste():
    if request.method == 'POST':
        if not request.is_json:
            return {"msg": "Formato enviado não corresponde a um JSON"}
        
        set_teste(request['nome'])
        return 'Teste inserido com sucesso'
    
    return get_teste()

if __name__ == '__main__':
 app.run(host='127.0.0.1', port=8080, debug=True)
