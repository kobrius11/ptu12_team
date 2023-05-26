from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/renaldas_zvega')
def renaldas():
    return render_template('renaldas_zvega.html')

if __name__ == "__main__":
    app.run(debug=True)
