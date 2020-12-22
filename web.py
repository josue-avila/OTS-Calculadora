from flask import Flask, render_template
from calculadora import plus, minus, multiplication, division

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/soma')
def web_sum():
    value1 = 2.0
    value2 = 3.0
    result = plus(value1, value2)
    return render_template('sum.html', v1=value1, v2=value2, r = result)

@app.route('/subtracao')
def web_subtract():
    value1 = 2.0
    value2 = 3.0
    result = minus(value1, value2)
    return render_template('subtract.html', v1=value1, v2=value2, r =result)

@app.route('/multiplicacao')
def web_multiply():
    value1 = 2.0
    value2 = 3.0
    result = multiplication(value1, value2)
    return render_template('multiply.html', v1=value1, v2=value2, r =result)

@app.route('/divisao')
def iweb_divide():
    value1 = 2.0
    value2 = 3.0
    result = division(value1, value2)
    return render_template('divide.html', v1=value1, v2=value2, r =result)


app.run(debug=True)