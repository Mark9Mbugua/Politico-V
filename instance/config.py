import os

class Config:
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True 
    SECRET = os.getenv('SECRET')
    DEBUG = True
    DATABASE_URL = 'postgresql://postgres:1998@localhost:5432/politico_db'

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing."""
    DATABASE_URL='postgresql://postgres:1998@localhost:5432/test_politico_db'
    DEBUG = True
    TESTING = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DATABASE_URL = 'postgres://rijnwynnsgereo:c1f5a57137914767efad6d5680dfe17a777ea8cf19bc0fcc7353d63faf752023@ec2-50-17-193-83.compute-1.amazonaws.com:5432/ddf76a2aiq5md3'

    DEBUG = False
    TESTING = False

app_config = {  
                'development': DevelopmentConfig,
                'testing' : TestingConfig,
                'staging': StagingConfig,
                'production': ProductionConfig,
            }