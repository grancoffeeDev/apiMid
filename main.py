from flask import Flask, jsonify, request
from db import *

#https://www.smashingmagazine.com/2020/08/api-flask-google-cloudsql-app-engine/
#https://github.com/GoogleCloudPlatform/cloud-sql-python-connector
#https://cloud.google.com/sql/docs/postgres/connect-connectors#python_1
#https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#
#https://www.geeksforgeeks.org/setting-up-google-cloud-sql-with-flask/
#https://dev.to/gabrielosluz/get-data-from-cloud-sql-with-python-51jm

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
