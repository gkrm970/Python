from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)


class Flask:
    pass


def jsonify():
    return None


def request():
    return None


def current_app():
    return None