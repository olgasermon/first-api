from app import app

class Routes(object):

    @app.route('/')
    @app.route('/index')
    def index():
        return "Hello world!"
