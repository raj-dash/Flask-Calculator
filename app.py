from flask import Flask, render_template, request, url_for
from math import sin, cos, tan, sqrt, asin, acos, atan

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', home=True)

@app.route('/simple')
def simple():
    return render_template('simple.html')

@app.route('/calculate', methods=['post'])
def calculate():
    result = note = color = ''
    first = float(request.form['firstNumber'])
    operation = request.form['operation']
    second = float(request.form['secondNumber'])
    if operation == "plus":
        result = first + second
    elif operation == "minus":
        result = first - second
    elif operation == "multiply":
        result = first * second
    elif operation == "divide":
        result = first / second
    else:
        note = "Error has occured"
        color = "alert-danger"
    return render_template('simple.html', result=result, note=note, color=color)

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

@app.route('/calculate_advanced', methods=['post'])
def calculate_advanced():
    result = note = color = ''
    first = float(request.form['firstNumber'])
    operation = request.form['operation']
    try:
        if operation == "sin":
            result = sin(first)
        elif operation == "cos":
            result = cos(first)
        elif operation == "tan":
            result = tan(first)
        elif operation == "asin":
            result = asin(first)
        elif operation == "acos":
            result = acos(first)
        elif operation == "atan":
            result = atan(first)
        elif operation == "sqrt":
            result = sqrt(first)
        else:
            note = "Math Error has Occured"
            color = "alert-danger"
    except ValueError:
        note = "Math Error has Occured"
        color = "alert-danger"
    return render_template('advanced.html', result=result, note=note, color=color)

if __name__ == "__main__":
    app.run(debug=True)