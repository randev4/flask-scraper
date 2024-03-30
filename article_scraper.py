from flask import Blueprint, request, jsonify
from newspaper import Article

scrape_articles_route = Blueprint('article_scraper', __name__)

def scrape_articles(urls):
    results = []

    for url in urls:
        if not url.strip():
            continue

        article = Article(url)

        try:
            article.download()
            article.parse()

            results.append({
                'title': article.title,
                'url': url,
                'text': article.text
            })

        except Exception as e:
            results.append({
                'error': f'Failed to scrape {url}: {str(e)}'
            })

    return results

@scrape_articles_route.route('/scrape', methods=['POST'])
def scrape_articles_route_func():
    urls = request.json.get('urls', [])
    results = scrape_articles(urls)
    return jsonify(results)
