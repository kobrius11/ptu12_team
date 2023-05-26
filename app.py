from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vardenis_pavardenis/')
def vardenis_pavardenis():
    return render_template('vardenis_pavardenis.html/')

@app.route('/evelina_stonyte/')
def evelina_stonyte():
    return render_template('evelina_stonyte.html/')

if __name__ == "__main__":
    app.run(debug=True)
