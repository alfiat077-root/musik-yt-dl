import yt_dlp
import os
import time
import sys

# Animasi loading
def loading(text="Loading"):
    for i in range(3):
        sys.stdout.write(f"\r{text}{'.' * (i+1)}")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\r", end="")

# Animasi download
def animasi_download():
    for i in range(101):
        sys.stdout.write(f"\rDownloading: {i}%")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

# Input user
print("="*40)
print("🎵 YT MUSIC DOWNLOADER (MP3)")
print("="*40)

judul = input("Masukkan judul lagu: ")
path = input("Masukkan path penyimpanan (contoh /storage/emulated/0/Musik): ")

# Validasi path
if not os.path.exists(path):
    print("❌ Path tidak ditemukan!")
    exit()

loading("Mencari lagu")

# Opsi yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{path}/%(title)s.%(ext)s',
    'quiet': True,
    'noplaylist': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Cari video dari judul
        hasil = ydl.extract_info(f"ytsearch1:{judul}", download=False)
        video = hasil['entries'][0]
        url = video['webpage_url']

        print(f"\n🎧 Ditemukan: {video['title']}")
        print("🔽 Mulai download...")

        animasi_download()

        # Download
        ydl.download([url])

    print("\n✅ Selesai! Musik tersimpan di:")
    print(path)

except Exception as e:
    print(f"❌ Error: {e}")