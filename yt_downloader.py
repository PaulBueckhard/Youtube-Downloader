from pytube import YouTube
import os
import re

FORMAT = "mp4"  # mp4 or mp3
VIDEOS = [""]

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def download(format, videos):
    if format == "mp4":
        folder_name = "videos"
    elif format == "mp3":
        folder_name = "audios"
    else:
        print("Invalid format. Choose 'mp4' or 'mp3'")
        return

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    for video in videos:
        yt = YouTube(video)
        title = yt.title
        filename = sanitize_filename(title)

        if format == "mp4":
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=folder_name, filename=filename + ".mp4")
            print(f"Downloaded {filename} as video.")

        elif format == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path=folder_name, filename=filename + ".mp3")
            print(f"Downloaded {filename} as audio.")

download(FORMAT, VIDEOS)
