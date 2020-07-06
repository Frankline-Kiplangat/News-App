class Sources:
    """
    Source class to define the source of news
    """
    
    def __init__(self, id, title, description, url, newsCategory, language, country):
        self.id= id
        self.title = title
        self.description = description
        self.url = url
        self.newsCategory = newsCategory
        self.language = language
        self.country = country
        
        
class Articles:
    """
    Article class to define the news article
    """
    
    def __init__(self,id,author,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
