import os

class Config:
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True 
    SECRET = os.getenv('SECRET')
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Configurations for Testing."""
    DATABASE_URL= os.getenv('TEST_DATABASE_URL')
    DEBUG = True
    TESTING = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DATABASE_URL = os.getenv('PROD_DATABASE_URL')
    DEBUG = True
    TESTING = False

app_config = {  
                'development': DevelopmentConfig,
                'testing' : TestingConfig,
                'staging': StagingConfig,
                'production': ProductionConfig,
            }