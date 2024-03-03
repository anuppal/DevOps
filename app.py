# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)


"""A simple Flask application"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a simple 'Hello, World!' message."""
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)