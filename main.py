from flask import *
import os
import psycopg2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_gc_teste():
    return make_response(jsonify(mensagem='API do MID'))

# Tabela public.gc_teste
@app.route('/gc_teste', methods=['GET'])
def get_teste():
    conn = psycopg2.connect(
        host="34.95.183.152",
        database="TelemetriaGC",
        port="5432",
        user=os.environ['SQL_USER'],
        password="VnBgPQbYzwa95VDm")
    cur = conn.cursor()
    cur.execute('SELECT * FROM GC_TESTE;')
    return json.dumps(cur.fetchall(),indent=4)
    

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(host='127.0.0.1', port=8080, debug=True)
    #app.run()
