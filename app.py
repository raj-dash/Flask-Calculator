from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def calculate():
    ans=''
    if request.method=='POST':
        try:
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            operation = request.form.get('op').lower()
            if operation == 'add':
                ans = a+b
            elif operation == 'subtract':
                ans = a-b
            elif operation == 'multiply':
                ans = a*b
            elif operation == 'divide':
                ans = a/b
            else:
                ans = "Enter valid values"
        except ValueError:
            ans = "Enter Valid Values"
    return render_template('index.html', ansh=ans)

if __name__ == "__main__":
    app.run(debug=True)



