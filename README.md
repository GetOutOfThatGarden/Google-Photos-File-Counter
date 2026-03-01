# Google Photos File Counter (CLI)

A simple Python CLI tool that connects to your Google Photos account and counts all media items by file type / extension (e.g. JPG, PNG, HEIC, MP4, MOV).

---

## ⚠️ IMPORTANT (As of 2024+)

Google has significantly restricted access to the Google Photos Library API.

Even when:

- OAuth authentication succeeds
- You log in successfully in the browser
- A valid token.json is created

You may still receive:

HttpError 403: Request had insufficient authentication scopes

This is NOT a coding error.

Google now classifies the following scope as **Sensitive / Restricted**:

https://www.googleapis.com/auth/photoslibrary.readonly

Unverified apps can still authenticate, but are now blocked from calling certain API endpoints such as:

photoslibrary.googleapis.com/v1/mediaItems.list

This means:

Your login will succeed  
Your token will be valid  
But Google will refuse to return your photo library data

---

## 🧾 Why This Happens

To access mediaItems.list now, your app may require:

- OAuth App Verification
- Domain ownership verification
- A published Privacy Policy
- Google's Sensitive Scope Review
- In some cases, an external security assessment

Approval can take weeks and is not practical for personal one-off scripts.

---

## 🟩 Workaround

If your goal is to verify that photos were successfully migrated between accounts:

Use Google Takeout to export both accounts and compare the files locally instead.

This avoids:

- API restrictions
- OAuth scope limitations
- Verification requirements
- Future breakage

---

## 🚀 Setup Instructions

1. Create OAuth credentials in Google Cloud Console
2. Download the OAuth Desktop App JSON
3. Rename it to:

credentials.json

4. Place it inside this project directory

5. Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

6. Install dependencies:

pip install -r requirements.txt

7. Run the script:

python google_photos_counter.py

---

## 📌 Note

This tool may no longer function for unverified apps due to Google API policy changes.

