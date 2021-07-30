from flask import Flask, render_template

app = Flask(__name__)


# app.debug = True

@app.route('/')  # Endpoint
@app.route('/home')
@app.route('/welcome')
def hello_world():
    profile = {
        'fullname': 'Michael Jamie',
        'age': 13,
        'phone': 'Samsung'
    }
    numbers = [12, 34, 112, 23, 13, 100, 3848, 'jerry']
    return render_template('index.jinja2', name='Michael', numb=numbers, profile=profile )


@app.route('/about')
def about():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
