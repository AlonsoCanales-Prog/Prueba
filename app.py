from flask import Flask

app = Flask(__name__)

def home():
    return "Hola desde Render!"

if __name__=='main':
    app.run()