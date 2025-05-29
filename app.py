from googleapiclient.discovery import build

# Put your google cloud token below (for more information read readme file)
API_KEY = 'AIzaSyDwYK8-iFPS9aWH9I5vG6f7AbAaUJRXWow'
# Put the link of the playlist ID below you can get it from the link of the playlist
PLAYLIST_ID = 'PL-gJaEk33vQJOpYRkR5geI3UNoN7jJMHQ'

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_playlist_items(playlist_id):
    next_page_token = None
    while True:
        response = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in response['items']:
            title = item['snippet']['title']
            added_date = item['snippet']['publishedAt']
            print(f"{added_date} — {title}")

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

get_playlist_items(PLAYLIST_ID)
