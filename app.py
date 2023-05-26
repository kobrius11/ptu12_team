from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vardenis_pavardenis/')
def vardenis_pavardenis():
    return render_template('vardenis_pavardenis.html/')

@app.route('/zygimantas_bickus/')
def zygimantas_bickus():
    return render_template('zygimantas_bickus.html/')

if __name__ == "__main__":
    app.run(debug=True)
