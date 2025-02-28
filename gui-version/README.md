# YouTube Downloader GUI 🎥

A Python-based YouTube video and playlist downloader with a graphical user interface that retrieves videos in the highest available quality. Download single videos, entire playlists, or specific videos from playlists with ease.

## Features ✨

- **User-Friendly Interface**: Simple and intuitive GUI for easy interaction
- **Single Video Download**: Automatically selects and downloads the highest quality available
- **Playlist Support**: Preview playlist contents and select specific videos to download
- **Real-Time Progress**: Visual progress bar with download speed and ETA indicators
- **Detailed Logs**: Built-in log console to track download status and errors
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux

## Requirements 📋

- Python 3.6+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- tkinter (usually comes with Python)
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

Launch the application:

```bash
python youtube_downloader.py
```

### Application Workflow

1. **Enter URL**: Paste a YouTube video or playlist URL in the input field
2. **Check Playlist**: Click "Check Playlist" to retrieve video information
3. **Select Videos**: For playlists, select specific videos if desired
4. **Start Download**: Click "Start Download" to begin the download process
5. **Monitor Progress**: Track download progress, speed, and ETA in real-time
6. **View Logs**: Check the log console for detailed information and any errors

### Download Options

- **Download All**: Downloads all videos in a playlist
- **Download Selected**: Only downloads videos selected from the playlist list


## Folder Structure 📂

```
youtube_downloader/
├── youtube_downloader.py
├── README.md
├── screenshots/
│   └── app_screenshot.png
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
| GUI not responding | Wait for background operations to complete |
| Playlist not loading | Check your internet connection or try a different URL |

## License 📄

MIT License - See LICENSE file for details.

## Credits 🙌

- Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- GUI built with [tkinter](https://docs.python.org/3/library/tkinter.html)
- Audio/Video merging by [FFmpeg](https://ffmpeg.org/)

---

Enjoy your downloads! 🎉✨