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
    def __init__(self, id, title, author, description, url, urlToImage, publishedOn, content):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedOn = publishedOn
        self.content = content