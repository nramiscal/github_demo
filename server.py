from flask import Flask, render_template, redirect, session

app = Flask(__name__)

@app.route('/')
def index():
    x = 123
    return render_template('index.html')

app.run(debug=True)
