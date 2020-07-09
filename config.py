import os
class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey=fdee0f42def74c7bad48a87e16fd6f08'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=fdee0f42def74c7bad48a87e16fd6f08'

    NEWS_API_KEY = os.environ.get('fdee0f42def74c7bad48a87e16fd6f08')
    
    SECRET_KEY= os.environ.get('SECRET_KEY')

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