from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vardenis_pavardenis/')
def vardenis_pavardenis():
    return render_template('vardenis_pavardenis.html/')

@app.route('/arnas_bolisas/')
def arnas_bolisas():
    return render_template('arnas_bolisas.html')

if __name__ == "__main__":
    app.run(debug=True)
5