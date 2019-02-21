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
    DATABASE_URL = 'postgres://wxdaktrvhevvma:58c93ca91945a567e020f8ef8240d8668aa945ff255537f961d97059ce25d3bf@ec2-23-21-165-188.compute-1.amazonaws.com:5432/daulhq4hucu8ip'

    DEBUG = False
    TESTING = False

app_config = {  
                'development': DevelopmentConfig,
                'testing' : TestingConfig,
                'staging': StagingConfig,
                'production': ProductionConfig,
            }