from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # dgfsfdgs
    # todo
    # a.xxx()
    # a.xxx()
    # execute module code ...
    # result = ...
    return render_template("index.html", result='123', date='2018-03-30')

@app.route('/integration')
def integration():
    return render_template('integration/main.html')


@app.route('/shopping_cart')
def shopping_cart():
    return render_template('shopping_cart/main.html')

@app.route('/faq')
def faq():
    return render_template('faq/main.html')

@app.route('/step')
def step():
    return render_template('integration/step.html')



if __name__ == '__main__':
    app.run()
