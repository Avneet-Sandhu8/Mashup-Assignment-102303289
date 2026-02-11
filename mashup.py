import os
import shutil
import zipfile
from yt_dlp import YoutubeDL
from pydub import AudioSegment


def create_mashup(singer, num_videos, duration, output_name):

    # 🔒 Validation
    if num_videos <= 10:
        raise ValueError("Number of videos must be greater than 10")

    if duration <= 20:
        raise ValueError("Duration must be greater than 20 seconds")

    download_folder = "downloads"

    # 📁 Create downloads folder
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # 🧹 Clear old downloads
    for file in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # 🧹 Remove old output files
    mp3_filename = f"{output_name}.mp3"
    zip_filename = f"{output_name}.zip"

    if os.path.exists(mp3_filename):
        os.remove(mp3_filename)

    if os.path.exists(zip_filename):
        os.remove(zip_filename)

    # 🎵 Download audio from YouTube
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'quiet': True,
        'ignoreerrors': True
    }

    search_query = f"ytsearch{num_videos}:{singer} songs"

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

    # 🎧 Merge & trim audio
    final_audio = AudioSegment.empty()

    files = os.listdir(download_folder)

    if not files:
        raise Exception("No audio files downloaded. Try another singer.")

    for file in files:
        file_path = os.path.join(download_folder, file)

        try:
            audio = AudioSegment.from_file(file_path)
            trimmed = audio[:duration * 1000]
            final_audio += trimmed
        except Exception as e:
            print(f"Skipping file {file}: {e}")
            continue

    if len(final_audio) == 0:
        raise Exception("Failed to process audio files.")

    # 💾 Export final MP3
    final_audio.export(mp3_filename, format="mp3")

    # 📦 Create ZIP file
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(mp3_filename)

    # 🧹 Clean up
    shutil.rmtree(download_folder)
    os.remove(mp3_filename)

    # ✅ RETURN ZIP FILE NAME
    return zip_filename
