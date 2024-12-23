import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'CITS3403'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = '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'