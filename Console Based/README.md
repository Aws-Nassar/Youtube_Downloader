# YouTube Downloader 🎥

A Python-based YouTube video and playlist downloader that allows you to download videos in the highest available quality. Supports single videos, entire playlists, or specific playlist selections.


## Features ✨
- **Single Video Download**: Automatically downloads the highest quality available.
- **Playlist Support**: Download entire playlists or select specific videos using flexible syntax.
- **Real-Time Progress**: Displays download speed, progress bar, and ETA.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Requirements 📋
- Python 3.6+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- FFmpeg (optional but recommended for format merging)

## Installation 🛠️

### 1. Install Python
Ensure Python is installed: [python.org](https://www.python.org/)

### 2. Install yt-dlp
```bash
pip install yt-dlp

### 3. Install FFmpeg (Recommended)

Windows:
Download from ffmpeg.org, add to PATH

macOS:

```bash
brew install ffmpeg

Linux:

```bash
Copy
sudo apt install ffmpeg  # Debian/Ubuntu
sudo dnf install ffmpeg  # Fedora

Usage 🚀
bash
Copy
python youtube_downloader.py
Single Video Download
text
Copy
Enter YouTube URL: https://www.youtube.com/watch?v=example
[✔] Downloaded: "Video Title.mp4"
Playlist Download
text
Copy
Enter YouTube URL: https://www.youtube.com/playlist?list=example

Playlist detected with 3 videos:
1. Video Title 1
2. Video Title 2
3. Video Title 3

Download options:
1. Download entire playlist
2. Select specific videos
Choice (1/2): 2

Enter selection (e.g., 1,3,5-10): 1,3
[✔] Downloaded 2/2 videos
Folder Structure 📂
Copy
youtube_downloader/
├── youtube_downloader.py
├── README.md
└── downloads/
    ├── Video Title 1.mp4
    └── Best Tutorial.mp4
Troubleshooting 🔧
"URL not valid": Verify the URL format

Download errors: Check internet connection and dependencies

Merge issues: Ensure FFmpeg is installed and in PATH

License 📄
MIT License - See LICENSE for details.

Credits 🙌
Powered by yt-dlp

Audio/Video merging by FFmpeg

Enjoy your downloads! 🎉✨



