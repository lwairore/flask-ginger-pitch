import os
class Config:
    """
    General parent configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SENDGRID_MAIL_USERNAME = os.environ.get("SENDGRID_MAIL_USERNAME")
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}

