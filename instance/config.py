import os

class Config:
    """Parent configuration class."""
    DEBUG = False 
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True


app_config = {  
                'development': DevelopmentConfig,
                'testing' : TestingConfig
            }