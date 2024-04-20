

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_sum():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
            return render_template('result.html', result=result)
        except ValueError:
            return "Invalid input. Please enter valid numbers."
    return render_template('input_form.html')

if __name__ == '__main__':
    app.run(debug=True)
