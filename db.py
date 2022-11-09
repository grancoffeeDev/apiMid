import os
from flask import jsonify
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

# initialize connector
connector = Connector()

def getconn():
    
    conn = connector.connect(
    db_connection_name, # <PROJECT-ID>:<REGION>:<INSTANCE-NAME>
    "pg8000",
    user=db_user,
    password=db_password,
    db=db_name,
    ip_type=IPTypes.PUBLIC
    )
    
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

def get_teste():
    with pool.connect() as db_conn:
      results = db_conn.execute("select * from gc_teste").fetchall()
      connector.close()
      return results
  
def set_teste(name):
    insert_stmt = sqlalchemy.text("INSERT INTO gc_teste (nome) VALUES (:nome)")
    with pool.connect() as db_conn:
      db_conn.execute(insert_stmt, nome=name)
      results = db_conn.execute("select * from gc_teste").fetchall()
      connector.close()
      return results