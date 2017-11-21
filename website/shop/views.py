from . import shop


@shop.route('/')
def hello():
    return 'Hello World'
