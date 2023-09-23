from flask import Flask, render_template

app = Flask(__name__)

def index():
    # Process your data here
    data = [1, 2, 3, 4, 5]  # Replace with your actual data

    return render_template('index.html', data=data)
