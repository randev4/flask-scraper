from flask import Flask

app = Flask(__name__)

from .reddit_scraper import scrape_reddit_thread_route
from .article_scraper import scrape_articles_route

app.register_blueprint(scrape_reddit_thread_route)
app.register_blueprint(scrape_articles_route)
