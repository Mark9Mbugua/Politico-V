import os

class Config:
    """Parent configuration class."""
    DEBUG = False 
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL='postgresql://postgres:1998@localhost:5432/politico_db'

class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_URL='postgresql://postgres:1998@localhost:5432/test_politico_db'


app_config = {  
                'development': DevelopmentConfig,
                'testing' : TestingConfig
            }