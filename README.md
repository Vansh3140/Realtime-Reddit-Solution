# Reddit Search Application

## Overview
A powerful, user-friendly web application that enables users to search Reddit content through an intuitive interface. The application provides a two-step search process: first finding relevant subreddits, then searching within them for specific posts. Built with Flask and vanilla JavaScript, it uses Reddit's OAuth API for secure data fetching.

![Project Screen-recording]
https://realtime-reddit-solution.onrender.com
You can use the service here but as it is deployed on the free render version so it might take a minute to again up the service
https://github.com/user-attachments/assets/dabda77b-43cd-4ea3-b778-c330126cb69c



## Features

### Subreddit Search
- Real-time subreddit search with dynamic results
- Displays comprehensive subreddit information:
  - Subscriber count
  - Community description
  - Activity status
  - Custom subreddit icons
- Visual tags for popularity and activity levels
- Clickable subreddit cards for seamless navigation

### Post Search
- Advanced post search within selected subreddits
- Flexible search controls:
  - Multiple sorting options (relevance, hot, top, new)
  - Adjustable result limits (10, 25, 50, 100 posts)
- Rich post previews including:
  - Post title and excerpt
  - Author information
  - Vote count and comment statistics
  - Timestamps
  - Thumbnails (when available)
  - Flair tags and NSFW markers
- Direct links to original Reddit posts

### Technical Features
- Server-side credential management
- OAuth token handling with automatic refresh
- Rate limit compliance
- Error handling and user feedback
- Responsive design
- Cross-browser compatibility

## Technology Stack

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript
- Google Fonts (Roboto)

### Backend
- Python 3.x
- Flask
- python-dotenv
- requests

### APIs
- Reddit OAuth API
- Reddit JSON API

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Reddit API credentials (Client ID and Secret)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/reddit-search-app.git
cd reddit-search-app
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install flask python-dotenv requests
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory:
```
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
```

### Step 5: Organize Project Structure
Ensure your project structure matches the following:
```
reddit-search-app/
├── templates/
│   ├── index.html
│   └── search.html
├── static/
│   └── styles.css
├── server.py
├── .env
└── README.md
```

### Step 6: Run the Application
```bash
python server.py
```
Visit `http://localhost:5000` in your web browser.

## Configuration

### Reddit API Credentials
1. Visit https://www.reddit.com/prefs/apps
2. Click "create another app..."
3. Select "script"
4. Fill in the required information:
   - name: your_app_name
   - redirect uri: http://localhost:5000/callback
   - description: Optional description
5. Copy the generated Client ID and Secret to your `.env` file

### Server Configuration
The Flask server runs in debug mode by default. For production:
1. Set `debug=False` in `server.py`
2. Configure appropriate host and port settings
3. Implement proper security measures

## Usage

### Finding a Subreddit
1. Enter a keyword in the subreddit search box
2. Browse through the displayed subreddit cards
3. Click on a subreddit to search within it

### Searching Posts
1. Enter search terms in the post search box
2. Select desired sorting method and result limit
3. Click "Search Posts" to view results
4. Click "View Post" on any result to open the original Reddit post

## Security Considerations
- API credentials are stored server-side
- OAuth tokens are managed securely
- User input is sanitized
- Error messages are user-friendly without exposing sensitive information

## Error Handling
The application handles various error scenarios:
- Network connectivity issues
- API rate limiting
- Invalid searches
- Authentication failures
- Missing resources

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Known Issues
- Rate limiting may affect search response times
- Some subreddit icons may not load due to Reddit's CDN restrictions
- NSFW content filtering requires user authentication

## Future Enhancements
- User authentication
- Advanced search filters
- Comment previews
- Sort by custom time ranges
- Subreddit statistics
- Post analytics
- Mobile app version

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Reddit API Documentation
- Flask Documentation
- Python Requests Library
- Contributors and testers

## Support
For support, please:
1. Check existing issues
2. Create a new issue with detailed information
3. Join our community discussions

---
Made with ❤️ by Vansh Singh Chaudhary
