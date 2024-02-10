from flask import Flask, request, jsonify
from newspaper import Article

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape_articles():
    # Retrieve URLs from the JSON request body
    urls = request.json.get('urls', [])
    
    # Initialize an empty list to hold the results
    results = []

    for url in urls:
        # Skip empty lines
        if not url.strip():
            continue

        # Create an Article object
        article = Article(url)

        try:
            # Download and parse the article
            article.download()
            article.parse()

            # Append the result for this article to the results list
            results.append({
                'title': article.title,
                'url': url,
                'text': article.text
            })

        except Exception as e:
            # Append the error message for this URL to the results list
            results.append({
                'error': f'Failed to scrape {url}: {str(e)}'
            })

    # Return the results as JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
