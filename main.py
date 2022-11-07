from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_gc_teste():
    return make_response(jsonify(mensagem='Testando essa API'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
