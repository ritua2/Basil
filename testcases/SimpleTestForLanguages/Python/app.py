# app.py
# Armaan Cheema

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Basil!"

if __name__ == '__main__':
    app.run()
