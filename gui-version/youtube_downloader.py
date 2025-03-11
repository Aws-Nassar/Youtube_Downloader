import yt_dlp
import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from threading import Thread
from queue import Queue

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.state('zoomed')
        
        self.playlist_entries = []
        self.selected_items = []
        self.download_queue = Queue()
        
        self.create_widgets()
        self.check_for_updates()

    def create_widgets(self):
        # URL Input
        url_frame = ttk.Frame(self.root)
        url_frame.pack(pady=10, fill=tk.X)
        
        ttk.Label(url_frame, text="YouTube URL:").pack(side=tk.LEFT, padx=5)
        self.url_entry = ttk.Entry(url_frame, width=50)
        self.url_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        self.check_btn = ttk.Button(url_frame, text="Check Playlist", command=self.check_playlist)
        self.check_btn.pack(side=tk.LEFT, padx=5)

        # Playlist Listbox
        self.list_frame = ttk.LabelFrame(self.root, text="Playlist Videos")
        self.list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.playlist_list = tk.Listbox(self.list_frame, selectmode=tk.MULTIPLE)
        self.playlist_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Download Options
        options_frame = ttk.Frame(self.root)
        options_frame.pack(pady=10, fill=tk.X)
        
        self.download_type = tk.StringVar(value='all')
        ttk.Radiobutton(options_frame, text="Download All", variable=self.download_type, value='all').pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(options_frame, text="Download Selected", variable=self.download_type, value='selected').pack(side=tk.LEFT, padx=5)
        
        # Progress Area
        progress_frame = ttk.LabelFrame(self.root, text="Download Progress")
        progress_frame.pack(pady=10, fill=tk.BOTH)
        
        self.progress_bar = ttk.Progressbar(progress_frame, mode='determinate')
        self.progress_bar.pack(fill=tk.X, padx=5, pady=5)
        
        self.status_label = ttk.Label(progress_frame, text="Ready")
        self.status_label.pack(pady=5)
        
        self.speed_label = ttk.Label(progress_frame, text="Speed: -")
        self.speed_label.pack(pady=2)
        
        self.eta_label = ttk.Label(progress_frame, text="ETA: -")
        self.eta_label.pack(pady=2)

        # Log/Status Console
        self.log_area = scrolledtext.ScrolledText(self.root, height=8, state='disabled')
        self.log_area.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Download Button
        self.download_btn = ttk.Button(self.root, text="Start Download", command=self.start_download)
        self.download_btn.pack(pady=10)

    def check_playlist(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return
        
        Thread(target=self.fetch_playlist_info, args=(url,), daemon=True).start()
        self.log("Checking playlist...")

    def fetch_playlist_info(self, url):
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': True
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                if 'entries' in info:
                    self.playlist_entries = info['entries']
                    self.root.after(0, self.update_playlist_list)
                    self.log(f"Found {len(self.playlist_entries)} videos in playlist")
                else:
                    self.root.after(0, lambda: self.log("Single video detected"))
        except Exception as e:
            self.root.after(0, lambda: self.log(f"Error: {str(e)}"))
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))

    def update_playlist_list(self):
        self.playlist_list.delete(0, tk.END)
        for entry in self.playlist_entries:
            self.playlist_list.insert(tk.END, entry.get('title', 'Untitled'))

    def start_download(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return
        
        if self.download_type.get() == 'selected':
            selected = self.playlist_list.curselection()
            if not selected:
                messagebox.showerror("Error", "Please select videos to download")
                return
            playlist_items = ",".join([str(i+1) for i in selected])
        else:
            playlist_items = None
        
        Thread(target=self.run_download, args=(url, playlist_items), daemon=True).start()
        self.toggle_controls(False)
        self.log("Starting download...")

    def run_download(self, url, playlist_items):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'progress_hooks': [self.progress_hook],
            'ignoreerrors': True,
            'noprogress': True
        }
        
        if playlist_items:
            ydl_opts['playlist_items'] = playlist_items
        
        os.makedirs('downloads', exist_ok=True)

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.root.after(0, lambda: self.log("\nDownload completed successfully!"))
        except Exception as e:
            self.root.after(0, lambda: self.log(f"\nError occurred: {str(e)}"))
        finally:
            self.root.after(0, lambda: self.toggle_controls(True))

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            self.download_queue.put((
                d.get('_percent_str', '0%'),
                d.get('_speed_str', '?'),
                d.get('_eta_str', '?')
            ))
        elif d['status'] == 'finished':
            self.download_queue.put(('finished', d['filename']))

    def check_for_updates(self):
        while not self.download_queue.empty():
            data = self.download_queue.get()
            if data[0] == 'finished':
                self.log(f"\nFinalizing: {data[1]}")
            else:
                percent, speed, eta = data
                self.progress_bar['value'] = float(percent.strip('%'))
                self.status_label.config(text=f"Downloading: {percent}")
                self.speed_label.config(text=f"Speed: {speed}")
                self.eta_label.config(text=f"ETA: {eta}")
        self.root.after(100, self.check_for_updates)

    def toggle_controls(self, state):
        state = 'normal' if state else 'disabled'
        self.url_entry['state'] = state
        self.check_btn['state'] = state
        self.playlist_list['state'] = state
        self.download_btn['state'] = state

    def log(self, message):
        self.log_area['state'] = 'normal'
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
        self.log_area['state'] = 'disabled'

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
