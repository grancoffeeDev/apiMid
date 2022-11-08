from flask import *
from connection.config import Database

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_gc_teste():
    return make_response(jsonify(mensagem='Testando essa API !!'))

# Tabela public.gc_teste
@app.route('/gc_teste', methods=['GET'])
def get_teste():
   query = "select * from public.gc_teste"
   db = Database()
   db.connect()
   r = db.executar(query, '', 'GET')
   db.close()
   return json.loads(r)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    #app.run(host='127.0.0.1', port=8080, debug=True)
#app.run()
