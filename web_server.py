from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/results')
def results():
    return render_template('results.html', title='Results')


@app.route('/docs')
def docs():
    return render_template('docs.html', title='Docs')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
