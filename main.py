from flask import *
import psycopg2
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_gc_teste():
    return make_response(jsonify(mensagem='API do MID'))

# Tabela public.gc_teste
@app.route('/gc_teste', methods=['GET'])
def get_teste():
    conn = psycopg2.connect(
        host="10.92.160.5",
        database="TelemetriaGC",
        user="postgres",
        password="VnBgPQbYzwa95VDm")
    cur = conn.cursor()
    cur.execute('SELECT * FROM GC_TESTE;')
    p = json.dumps(cur.fetchall(),indent=4) 
    cur.close()
    conn.close()
    return p

@app.route('/gc_config', methods=['GET'])
def get_teste():
    conn = psycopg2.connect(
        host="35.247.217.164",
        database="grancoffee",
        user="postgres",
        password="VnBgPQbYzwa95VDm")
    cur = conn.cursor()
    cur.execute('select * from public.gc_config;')
    p = json.dumps(cur.fetchall(),indent=4) 
    cur.close()
    conn.close()
    return p

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    #app.run(host='127.0.0.1', port=8080, debug=True)
    #app.run()
