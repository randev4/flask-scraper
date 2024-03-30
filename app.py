from flask import Flask, jsonify

from .reddit_scraper import scrape_reddit_thread_route
from .article_scraper import scrape_articles_route

app = Flask(__name__)

app.register_blueprint(scrape_reddit_thread_route)
app.register_blueprint(scrape_articles_route)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the scraping application!'})

if __name__ == '__main__':
    app.run(debug=True)
