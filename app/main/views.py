from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles, search_artciles
from ..models import Articles, Sources

# Views
@main.route('/')
def index():

    """
    Function that returns the index page and its data
    """
    general_categories = get_sources()

    
    title = 'News Highlights'
    search_articles = request.args.get('articles_querry')
    if search_articles:
        return redirect(url_for('search', articles_name=search_articles))
    else:
        return render_template('index.html',title = title, general = general_categories)

@main.route('/newsarticle/<id>')
def newsarticle(id):

    """
    View article page function that returns the article details page and its data
    """
    articles_items = get_articles(id)
    title = f'{id} | News Articles'
    return render_template('newsarticle.html',title = title,articles = articles_items)

@main.route('/search/<articles_feed>')
def search(articles_feed):
    search_list = articles_feed.split(" ")
    title_format = "+".join(search_list)
    search_articles = get_articles(title_format)
    title = 'News results'
    search_articles = request.args.get('articles_search')
    if search_articles:
        return redirect(url_for('main.search',articles_feed=search_articles))
    else:
        return render_template('search.html',related=search_articles,title=title)


