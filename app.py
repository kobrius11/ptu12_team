from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Andrius_Gedvilas/')
def andrius_gedvilas():
    return render_template('Andrius_Gedvilas.html')

@app.route('/karolis_venckus/')
def karolis_venckus():
    return render_template('karolis_venckus.html')

@app.route('/renaldas_zvega')
def renaldas():
    return render_template('renaldas_zvega.html')

@app.route('/mantvydas/')
def mantvydas():
    return render_template('mantvydas.html/')

@app.route('/vardenis_pavardenis/')
def vardenis_pavardenis():
    return render_template('vardenis_pavardenis.html')

@app.route('/bronius_grigaras/')
def bronius_grigaras():
    return render_template('bronius_grigaras.html')

@app.route('/evelina_stonyte/')
def evelina_stonyte():
    return render_template('evelina_stonyte.html/')

if __name__ == "__main__":
    app.run(debug=True)
5