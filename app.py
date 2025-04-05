from flask import Flask

app = Flask(__name__)

@app.route("/")  # Esto define la ruta de la aplicación
def home():
    return "Hola desde Render!"

if __name__ == "__main__":  # Corregido
    app.run(host="0.0.0.0", port=10000)  # Render usa un puerto asignado automáticamente
