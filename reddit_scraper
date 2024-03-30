from flask import Blueprint, request, jsonify
import praw
import pyperclip
import io
import sys
import textwrap
import os

scrape_reddit_thread_route = Blueprint('reddit_scraper', __name__)

reddit = praw.Reddit(
    client_id="IPia2etSZTz27zOlOKyJww",
    client_secret="wQiyfkahCYSbSnGgI5wOVHhvygOHvA",
    user_agent="rdb scraper by randev4"
)

def scrape_reddit_thread(url):
    submission = reddit.submission(url=url)

    # Create a string buffer and redirect stdout to it
    buffer = io.StringIO()
    sys.stdout = buffer

    # Get the subreddit details
    print(f"Subreddit: r/{submission.subreddit.display_name}")
    print(f"Description: {submission.subreddit.public_description}")

    # Print the thread title, post content, and poster
    print(f"Reddit thread title: {submission.title}")
    print(f"Post content: {submission.selftext}")
    print(f"Posted by: {submission.author}")

    submission.comments.replace_more(limit=None)

    def print_comments(comments, level=0):
        for comment in comments:
            # Remove blank lines and make each comment just one paragraph
            comment_body = ' '.join(line.strip() for line in comment.body.split('\n') if line.strip())
            comment_body = textwrap.fill(comment_body, width=80)  # wrap the text after 80 characters
            print(' ' * level + f'Comment by {comment.author}: {comment_body}')
            if len(comment.replies) > 0:
                print_comments(comment.replies, level + 1)

    print_comments(submission.comments)

    # Reset stdout to its original value
    sys.stdout = sys.__stdout__

    # Return the contents of the buffer
    return buffer.getvalue()

@scrape_reddit_thread_route.route('/rscraper', methods=['POST'])
def scrape_reddit_thread_route_func():
    # Retrieve the URL from the JSON request body
    url = request.json.get('url')

    if not url or not url.strip():
        return jsonify({'error': 'Please provide a valid URL'}), 400

    try:
        script = scrape_reddit_thread(url)
        return jsonify({'script': script})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
