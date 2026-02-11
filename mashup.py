import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment
import zipfile

def create_mashup(singer, num_videos, duration, output_name):

    if num_videos <= 10:
        raise ValueError("Number of videos must be greater than 10")

    if duration <= 20:
        raise ValueError("Duration must be greater than 20 seconds")

    download_folder = "downloads"

    # Create downloads folder if not exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # 🔥 CLEAR OLD DOWNLOADS
    for file in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # 🔥 REMOVE OLD OUTPUT FILES (if exist)
    if os.path.exists(f"{output_name}.mp3"):
        os.remove(f"{output_name}.mp3")

    if os.path.exists(f"{output_name}.zip"):
        os.remove(f"{output_name}.zip")

    # Download videos
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
    'quiet': True,
    'ignoreerrors': True
}


    search_query = f"ytsearch{num_videos}:{singer} songs"

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

    # Merge audio
    final_audio = AudioSegment.empty()

    for file in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file)

        try:
            audio = AudioSegment.from_file(file_path)
            trimmed = audio[:duration * 1000]
            final_audio += trimmed
        except Exception as e:
            print(f"Skipping file {file}: {e}")
            continue

    output_path = f"{output_name}.mp3"
    final_audio.export(output_path, format="mp3")

    # Create ZIP file
    zip_filename = f"{output_name}.zip"

    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(output_path)

    return zip_filename
