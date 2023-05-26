from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Andrius_Gedvilas/')
def vardenis_pavardenis():
    return render_template('Andrius_Gedvilas.html/')

if __name__ == "__main__":
    app.run(debug=True)
