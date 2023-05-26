from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/petras_ans/')
def petras_anskaitis():
    return render_template('petras_ans.html/')

if __name__ == "__main__":
    app.run(debug=True)
