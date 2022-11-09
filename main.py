from flask import *
import psycopg2
import json
from google.cloud.sql.connector import Connector
import sqlalchemy

app = Flask(__name__)

INSTANCE_CONNECTION_NAME = "vmgc-e-commerce:southamerica-east1:middleware-pgsql"
DB_USER = "postgres"
DB_PASS = "VnBgPQbYzwa95VDm"
DB_NAME = "TelemetriaGC"

connector = Connector()

def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pg8000",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

@app.route('/', methods=['GET'])
def get_gc_teste():
    return make_response(jsonify(mensagem='API do MID'))

@app.route('/gc_config', methods=['GET'])
def get_teste():
    with pool.connect() as db_conn:
       results = db_conn.execute("SELECT * FROM gc_teste").fetchall()
       connector.close()
       return results

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    #app.run(host='127.0.0.1', port=8080, debug=True)
    #app.run()
