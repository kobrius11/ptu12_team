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

@app.route('/vardenis_pavardenis/')
def vardenis_pavardenis():
    return render_template('vardenis_pavardenis.html')

@app.route('/robertas_sapronavicius/')
def robertas_sapronavicius():
    return render_template('robertas_sapronavicius.html')

@app.route('/mindaugas_turauskas/')
def mindaugas_turauskas():
    return render_template('mindaugas_turauskas.html/')

@app.route('/milda_auglyte/')
def milda_auglyte():
    return render_template('milda_auglyte.html/')

@app.route('/arnas_bolisas/')
def arnas_bolisas():
    return render_template('arnas_bolisas.html')

@app.route('/karolis_jasadavicius/')
def karolis_jasadavicius():
    return render_template('karolis_jasadavicius.html/')

if __name__ == "__main__":
    app.run(debug=True)
5