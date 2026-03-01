import os
from collections import Counter
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

def main():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('photoslibrary', 'v1', credentials=creds)

    next_page_token = None
    ext_counter = Counter()
    type_counter = Counter()

    print("Scanning Google Photos library...\n")

    while True:
        results = service.mediaItems().list(pageSize=100, pageToken=next_page_token).execute()
        items = results.get('mediaItems', [])
        for item in items:
            filename = item.get('filename', '')
            mime = item.get('mimeType', '')
            ext = os.path.splitext(filename)[1].lower() or mime.split('/')[-1]

            ext_counter[ext] += 1
            type_counter['video' if 'video' in mime else 'photo'] += 1

        next_page_token = results.get('nextPageToken')
        if not next_page_token:
            break

    print("\n=== Total by type ===")
    for k,v in type_counter.items():
        print(f"{k}: {v}")

    print("\n=== Total by extension ===")
    for k,v in ext_counter.most_common():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
