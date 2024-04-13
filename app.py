from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            number = int(request.form.get('number'))
            if number <= 0:
                return render_template('index.html', error="Number should be positive.")
            if number > 100:
                return render_template('index.html', error="Number should be less than or equal to 100.")
            fibonacci_series = fibonacci(number)
            return render_template('index.html', fibonacci_series=fibonacci_series)
        except ValueError:
            return render_template('index.html', error="Invalid input. Please provide a valid number.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
