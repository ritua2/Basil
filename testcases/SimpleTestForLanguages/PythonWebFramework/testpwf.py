# Python Web Framework (Flask) test case

from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/')
def index():
    return str(add(2, 3))  # Expected output: 5

if __name__ == '__main__':
    app.run()
