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
            return jsonify({"msg": "Formato enviado não corresponde a um JSON"}), 400
        
        set_teste(request['nome'])
        return 'Teste inserido com sucesso'
    
    return get_teste()

if __name__ == '__main__':
 app.run(debug=True)
