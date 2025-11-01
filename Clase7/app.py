from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def home():
    datos={'usuarios':120,'ventas':4720,'visitas':3080}
    return render_template('home.html',datos=datos)
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')
else:
    print("El servidor está corriendo...")