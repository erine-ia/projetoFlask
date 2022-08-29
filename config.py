import os.path
base_dir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(base_dir, 'banco.db')

SQLALCHEMY_TRACK_MODIFICATIONS = True

