class Config:
    pass

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'DATABASE_URL'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = "/static"
    TEMPLATE_FOLDER = "/templates"
    SECRET_KEY = 'SECRET_KEY'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = "frontend/dist/static"
    TEMPLATE_FOLDER = "/frontend/dist/templates"
    SECRET_KEY = "kdsfklsmfakfmafmadslvsdfasdf"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
