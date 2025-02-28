import yt_dlp
import os

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']} | Speed: {d['_speed_str']} | ETA: {d['_eta_str']}", end='', flush=True)
    elif d['status'] == 'finished':
        print(f"\nFinalizing: {d['filename']}")

def get_playlist_info(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)
    except Exception as e:
        print(f"Error retrieving playlist info: {e}")
        return None

def download_media():
    url = input("Enter YouTube URL: ").strip()
    if not url:
        print("Error: Please enter a valid URL")
        return

    # Check if it's a playlist
    info = get_playlist_info(url)
    playlist_items = None

    if info and 'entries' in info:
        entries = info['entries']
        print("\nPlaylist detected with the following videos:")
        for idx, entry in enumerate(entries, 1):
            print(f"{idx}. {entry.get('title', 'Untitled')}")

        print("\nDownload options:")
        print("1. Download entire playlist")
        print("2. Select specific videos")
        choice = input("Enter your choice (1/2): ").strip()

        if choice == '2':
            print("\nEnter video numbers (e.g., 1,3,5-10):")
            playlist_items = input("Your selection: ").strip()

    # Set up download options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'ignoreerrors': True
    }

    if playlist_items:
        ydl_opts['playlist_items'] = playlist_items

    os.makedirs('downloads', exist_ok=True)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\nStarting download...")
            ydl.download([url])
        print("\nDownload completed successfully!")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")

if __name__ == "__main__":
    download_media()