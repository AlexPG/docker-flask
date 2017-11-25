import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my super secret key!!!'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    user = os.environ['POSTGRES_USER']
    pwd = os.environ['POSTGRES_PASSWORD']
    db = os.environ['POSTGRES_DB']
    host = 'db'
    port = '5432'
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % \
        (user, pwd, host, port, db)


config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
