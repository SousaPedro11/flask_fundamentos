class Config:
    SECRET_KEY = 'Miguel@12345'
    USERNAME = 'iec_desenv'
    PASSWORD = 'iec_desenv'
    SERVER = 'localhost'
    DB = 'flask_fundamentos'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
