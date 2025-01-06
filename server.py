from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests
from base64 import b64encode

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Proxy configuration
PROXY ={
    "http": f"http://{os.getenv('PROXIES')}",
    "https": f"http://{os.getenv('PROXIES')}",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/api/access_token', methods=['POST'])
def get_access_token():
    try:
        client_id = os.getenv('REDDIT_CLIENT_ID')
        client_secret = os.getenv('REDDIT_CLIENT_SECRET')
        
        auth = b64encode(f"{client_id}:{client_secret}".encode()).decode()
        
        headers = {
            'Authorization': f'Basic {auth}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        data = {'grant_type': 'client_credentials'}
        
        response = requests.post(
            'https://www.reddit.com/api/v1/access_token',
            headers=headers,
            data=data,
            proxies=PROXY  # Use proxy here
        )
        
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search_subreddits')
def search_subreddits():
    try:
        query = request.args.get('q')
        response = requests.get(
            f'https://www.reddit.com/subreddits/search.json?q={query}&type=sr&typeahead_active=true',
            proxies=PROXY  # Use proxy here
        )
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search_posts')
def search_posts():
    try:
        token = request.headers.get('Authorization').split(' ')[1]
        subreddit = request.args.get('subreddit')
        query = request.args.get('q')
        sort = request.args.get('sort', 'relevance')
        limit = request.args.get('limit', 25)
        
        headers = {'Authorization': f'Bearer {token}'}
        
        response = requests.get(
            f'https://oauth.reddit.com/r/{subreddit}/search',
            headers=headers,
            params={
                'q': query,
                'restrict_sr': 'true',
                'sort': sort,
                'limit': limit
            },
            proxies=PROXY  # Use proxy here
        )
        
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
