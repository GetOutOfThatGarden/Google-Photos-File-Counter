# Google Photos File Counter

A simple Python CLI tool to count all photos and videos in your Google Photos account by:

- Media type (photo vs video)
- File extension (.jpg, .png, .heic, .mp4, .mov, etc)

This tool uses the Google Photos Library API in read-only mode.

---

## Why This Exists

When migrating from one Google Photos account to another (e.g. using Partner Sharing), there is no built-in way to verify that:

- all photos transferred successfully
- all videos transferred successfully
- nothing is missing before deleting the original account

This tool allows you to audit your library by comparing media counts by extension and type.

---

## Setup Instructions

### 1. Create Google Cloud OAuth Credentials

Go to:

https://console.cloud.google.com/

Create:

- A new project
- Enable the Google Photos Library API
- Create an OAuth Client ID
- Application type: Desktop App

Download the OAuth credentials JSON file and rename it:

credentials.json

Place this file in the same folder as the script.

---

### 2. Install Dependencies

python3 -m venv venv  
source venv/bin/activate  
pip install google-auth-oauthlib google-api-python-client google-auth-httplib2  

---

### 3. Configure OAuth Consent Screen

Go to:

APIs & Services → OAuth Consent Screen

Set:

Publishing Status = Testing

Then go to:

Audience → Test Users

Add the Google account you want to scan.

---

## ⚠️ Known Issue: Some Google Accounts Cannot Be Added as Test Users

Some older or security-flagged Google accounts cannot be added as OAuth test users.

You may see an error like:

Ineligible accounts not added

This occurs because:

- Google blocks certain accounts from accessing unverified apps
- Accounts with legacy or internal security flags may be treated as sensitive
- Testing-mode OAuth apps are not allowed to request access to these accounts
- Google applies internal eligibility checks to reduce abuse of unverified apps

This means:

- You may be able to log into Google Cloud Console with the account
- You may be able to create OAuth credentials
- But still be prevented from authenticating via the OAuth flow

This is a Google-side restriction and cannot be overridden.

If this happens:

- Export the account using Google Takeout
- Perform verification locally instead

---

## Usage

python google_photos_counter.py

A browser window will open to authenticate your account.

After scanning completes, results will be printed in the terminal.

---

## Security

Do NOT commit your OAuth credentials.

This repository ignores:

- credentials.json
- venv/
- .env
- Python cache files

