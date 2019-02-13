import os

class Config:
    """Parent configuration class."""
    DEBUG = False 
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DEVELOPMENT = True
    
class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEVELOPMENT = True
    DEBUG = True

app_config = {  
                'development': DevelopmentConfig,
                'testing' : TestingConfig,
                'staging': StagingConfig
            }