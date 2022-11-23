from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

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

if __name__ == "__main__":
    app.run(debug=True)