🎵 YT Music Downloader (MP3)

Simple, fast, and lightweight Python tool to search and download music from YouTube directly as high-quality MP3 files.


🚀 Features

- 🔍 Search music by title (no need to copy links)
- 🎧 Auto-select best result from YouTube
- 🎵 Convert to MP3 (192kbps)
- 📂 Custom save directory
- ⚡ Fast download using "yt-dlp"
- 🎨 Terminal animation (loading + progress)


📦 Requirements

Make sure you have:

- Python 3.8+
- "ffmpeg" installed
- Internet connection

🔧 Installation

1. Clone repository

git clone https://github.com/alfiat077-root/musik-yt-dl
cd musik-yt-dl 

2. Install dependencies

pip install yt-dlp

3. Install FFmpeg

Termux:

pkg install ffmpeg

Linux:

sudo apt install ffmpeg

Windows:

Download from:
https://ffmpeg.org/download.html

▶️ Usage

Run the script:

python rapid.py

Then input:

Masukkan judul lagu: Alan Walker Faded
Masukkan path penyimpanan: /storage/emulated/0/Music

📂 Output

Downloaded file will be saved as:

/Music/Nama Lagu.mp3

⚙️ How It Works

1. User inputs song title
2. Script searches YouTube using "yt-dlp"
3. Picks the first result
4. Extracts best audio
5. Converts to MP3 using FFmpeg
6. Saves to selected directory

🎨 Preview

🎵 YT MUSIC DOWNLOADER (MP3)

Masukkan judul lagu: DJ Tiktok Viral
Masukkan path: /storage/emulated/0/Music

🔍 Mencari lagu...
🎧 Ditemukan: DJ Viral 2024
🔽 Mulai download...
Downloading: 100%

✅ Selesai!


⚠️ Notes

- Make sure the output directory exists
- Internet connection is required
- This tool uses public YouTube data
- For personal use only

📌 TODO / Future Features

- [ ] Multi-result selection (Top 5 search)
- [ ] Real progress bar (not simulated)
- [ ] Auto metadata (artist, album, cover)
- [ ] Playlist support
- [ ] GUI version

---

👤 Author

piat

⭐ Support

If you like this project:

- ⭐ Star this repo
- 🍴 Fork it
- 🛠️ Contribute improvements


📜 License

This project is licensed under the MIT License.


⚡ Disclaimer

This tool is created for educational and personal use only.
Users are responsible for how they use this software.