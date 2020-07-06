import os
class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'
    ARTICLES_API_BASE_URL  = 'https://newsapi.org/v2/articles?q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('fdee0f42def74c7bad48a87e16fd6f08')
    SECRET_KEY = os.environ.get('1234')

class ProdConfig(Config):
    """
    Pruduction  configuration child class

    """
        
    pass
    
class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = True
config_options = {
 'development' : DevConfig,
 'production' : ProdConfig
}