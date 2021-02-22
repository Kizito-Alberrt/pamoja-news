class Config:
    '''
    general configuration parent class
    '''
    pass
    NEWS_API_KEY ='<25221838d1aa461f9f76318460d92471>'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True