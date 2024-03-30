# views.py
from flask import jsonify
from . import app  # Import the app instance from __init__.py

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the scraping application!'})
