import os
class Config:
    '''
    general configuration parent class
    '''
    
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/everything?q=tesla&from=2021-01-25&sortBy=publishedAt&apiKey=25221838d1aa461f9f76318460d92471'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}