import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result/')
def result():
    heads_or_tails = random.randint(1, 2)
    result_text = 'شیر' if heads_or_tails == 1 else 'خط'
    return render_template('result.html', result_text=result_text)