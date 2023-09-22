from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def home():
    return "test"

if __name__ == '__main__':
    app.run(debug=True)