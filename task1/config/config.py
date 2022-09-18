from os import environ

class Config:
    ENV = environ.get('TASK1_ENV', 'production')
    DEBUG = bool(int(environ.get('TASK1_DEBUG', '0')))
    TESTING = DEBUG
    SESSION_PERMANENT = bool(int(environ.get('TASK1_SESSION_PERMANENT', '0')))
    SESSION_TYPE = environ.get('TASK1_SESSION_TYPE', 'filesystem')
