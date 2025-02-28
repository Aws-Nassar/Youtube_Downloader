# YouTube Downloader 🎥

A Python-based YouTube video and playlist downloader that retrieves videos in the highest available quality. Download single videos, entire playlists, or specific videos from playlists with ease.

## Features ✨

- **Single Video Download**: Automatically selects and downloads the highest quality available
- **Playlist Support**: Download entire playlists or select specific videos using flexible syntax
- **Real-Time Progress**: Displays download speed, progress bar, and ETA
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux

## Requirements 📋

- Python 3.6+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- FFmpeg (optional but recommended for format merging)

## Installation 🛠️

### 1. Install Python
Make sure Python is installed on your system: [python.org](https://www.python.org/)

### 2. Install yt-dlp
```bash
pip install yt-dlp
```

### 3. Install FFmpeg (Recommended)

**Windows:**
- Download from [ffmpeg.org](https://ffmpeg.org/download.html)
- Add to system PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
# Debian/Ubuntu
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

## Usage 🚀

Launch the downloader:
```bash
python youtube_downloader.py
```

### Single Video Download

```
Enter YouTube URL: https://www.youtube.com/watch?v=example
[✔] Downloaded: "Video Title.mp4"
```

### Playlist Download

```
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
```

## Folder Structure 📂

```
youtube_downloader/
├── youtube_downloader.py
├── README.md
└── downloads/
    ├── Video Title 1.mp4
    └── Best Tutorial.mp4
```

## Troubleshooting 🔧

| Issue | Solution |
|-------|----------|
| "URL not valid" | Verify the URL format is correct |
| Download errors | Check your internet connection and dependencies |
| Merge issues | Ensure FFmpeg is installed and in your system PATH |

## License 📄

MIT License - See LICENSE file for details.

## Credits 🙌

- Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Audio/Video merging by [FFmpeg](https://ffmpeg.org/)

---

Enjoy your downloads! 🎉✨
