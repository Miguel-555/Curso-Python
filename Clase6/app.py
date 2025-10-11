from flask import Flask
from login import login

app = Flask(__name__)
app.register_blueprint(login)

@app.route('/')
def home():
    return "Hola, Unida Experto en Python"
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')