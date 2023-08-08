from flask import Flask, request, jsonify

app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@app.route('/')
def home():
    return "Welcome to the Python Flask App!"

@app.route('/factorial/<int:number>')
def calculate_factorial(number):
    result = factorial(number)
    return jsonify({"number": number, "factorial": result})

@app.route('/fibonacci/<int:number>')
def calculate_fibonacci(number):
    result = fibonacci(number)
    return jsonify({"number": number, "fibonacci": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
