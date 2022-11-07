from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_gc_teste():
    return "oi"

app.run()
