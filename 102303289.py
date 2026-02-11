import sys
import os
import shutil
from yt_dlp import YoutubeDL
from pydub import AudioSegment
import zipfile


def download_videos(singer, num_videos):
    if os.path.exists("downloads"):
        shutil.rmtree("downloads")

    os.makedirs("downloads")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True
    }

    search_query = f"ytsearch{num_videos}:{singer} songs"

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


def convert_and_trim(duration):
    final_audio = AudioSegment.empty()

    for file in os.listdir("downloads"):
        file_path = os.path.join("downloads", file)

        try:
            audio = AudioSegment.from_file(file_path)
            trimmed_audio = audio[:duration * 1000]
            final_audio += trimmed_audio
        except Exception as e:
            print(f"Error processing {file}: {e}")

    return final_audio


def main():
    if len(sys.argv) != 5:
        print("Usage:")
        print("python 102303289.py <SingerName> <NumberOfVideos> <Duration> <OutputName>")
        sys.exit(1)

    singer = sys.argv[1]
    num_videos = int(sys.argv[2])
    duration = int(sys.argv[3])
    output_name = sys.argv[4]

    if num_videos <= 10:
        print("Number of videos must be greater than 10")
        sys.exit(1)

    if duration <= 20:
        print("Duration must be greater than 20 seconds")
        sys.exit(1)

    print("Downloading videos...")
    download_videos(singer, num_videos)

    print("Processing audio...")
    final_audio = convert_and_trim(duration)

    mp3_file = f"{output_name}.mp3"
    zip_file = f"{output_name}.zip"

    print("Exporting MP3...")
    final_audio.export(mp3_file, format="mp3")

    print("Creating ZIP file...")
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        zipf.write(mp3_file)

    print("Cleaning temporary files...")
    shutil.rmtree("downloads")
    os.remove(mp3_file)

    print(f"✅ Mashup created successfully: {zip_file}")


if __name__ == "__main__":
    main()

