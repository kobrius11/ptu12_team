from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/petras_ans/')
def petras_anskaitis():
    return render_template('petras_ans.html/')

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

@app.route('/bronius_grigaras/')
def bronius_grigaras():
    return render_template('bronius_grigaras.html')

@app.route('/zygimantas_bickus/')
def zygimantas_bickus():
    return render_template('zygimantas_bickus.html/')

@app.route('/deividas_skestenis/')
def deividas_skestenis():
    return render_template('deividas_skestenis.html')


@app.route('/raimonda_anisimova/')
def raimonda_anisimova():
    return render_template('raimonda_anisimova.html/')


@app.route('/evelina_stonyte/')
def evelina_stonyte():
    return render_template('evelina_stonyte.html/')

@app.route("/tadas_z/")
def tadas_z():
    return render_template("/tadas_z.html/")

@app.route('/jurate_krupaviciene/')
def jurate_krupaviciene():
    return render_template('jurate_krupaviciene.html/')

@app.route('/karolis_tamulevicius/')
def karolis_tamulevicius():
    return render_template('karolis_tamulevicius.html/')

if __name__ == "__main__":
    app.run(debug=True)