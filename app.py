from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Erikas_Jankauskas/')
def vardenis_pavardenis():
    return render_template('Erikas_Jankauskas.html/')

if __name__ == "__main__":
    app.run(debug=True)
