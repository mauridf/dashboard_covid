import os
class Config():
    CSRF_ENABLE = True
    SECRET = '02daa7d5d43ab2b968e0941563aaec9c4af9617734a8a31f'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = 'Dashboard COVID'

class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST,PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector:postgres:Mt190720@localhost:5432/dashboard_covid'

app_config = {
    'development': DevelopmentConfig(),
    'testing': None
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'