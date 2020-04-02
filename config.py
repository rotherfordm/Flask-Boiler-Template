import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '8d6703b7bee093c2d4fbdb3898eae3087046b051b728734ba4de9d7ebfbb05be'
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
