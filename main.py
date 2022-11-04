from fastapi import FastAPI
from model.teste import gcteste
from connection.config import Database
import json

#python -m uvicorn main:app --reload

app = FastAPI()

@app.get("/")
def home() :
    return {}

# Tabela public.gc_teste
@app.get("/gc_teste")
def get_teste():
   query = "select * from public.gc_teste"
   db = Database()
   db.connect()
   r = db.executar(query, '', 'GET')
   db.close()
   return json.loads(r)

@app.post("/gc_teste")
def post_teste(gc_teste: gcteste):
   query = "INSERT INTO public.gc_teste(nome) VALUES('{0}')".format(gc_teste.nome)
   db = Database()
   db.connect()
   db.executar(query, (gc_teste.nome), 'POST')
   db.close()
   return {"resultado":"Dados inseridos.", "nome":gc_teste.nome}
    
