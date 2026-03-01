# Google Photos Counter

A simple Python CLI tool to count all photos and videos in your Google Photos account by type and file extension.

## Setup

1. Create a Google Cloud project and download your OAuth credentials as `credentials.json`.

2. Install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install google-auth-oauthlib google-api-python-client google-auth-httplib2
