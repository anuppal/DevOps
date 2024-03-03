"""
This module defines a simple Flask application that prints 'Hello, World!' when accessed.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a simple 'Hello, World!' message."""
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
