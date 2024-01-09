import os
from tqdm import tqdm
import yt_dlp

def download_video_with_progress(url, download_path):
    ydl_opts = {
        'outtmpl': download_path,
        'progress_hooks': [hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def hook(d):
    if d['status'] == 'finished':
        print('\nDownload completed!')

def download_playlist(playlist_url, download_path='downloads'):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'progress_hooks': [hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")

    if "youtube.com/playlist" not in playlist_url:
        print("Invalid playlist URL. Please provide a valid YouTube playlist URL.")
    else:
        download_playlist(playlist_url)
