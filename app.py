from flask import Flask


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    @app.route('/')
    def hello():
        return 'Hello World'

    return app
