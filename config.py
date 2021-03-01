import os
class Config:
    '''
    general configuration parent class
    '''
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    EVERYTHING_API_BASE_URL = 'https://newsapi.org/v2/everything?domains=wsj.com&apikey={}'
    TOP_HEADLINES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    TECH_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={}'

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