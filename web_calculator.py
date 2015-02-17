from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('calculator.html')

@app.route('/result.html', methods=['POST', 'GET'])
def calculate():
    value1 = request.form['value1']
    value2 = request.form['value2']
    operator = request.form['operator']
    result = eval(value1 + operator + value2)

    return render_template('result.html'), result



if __name__ == "__main__":
    app.run(debug=True)
