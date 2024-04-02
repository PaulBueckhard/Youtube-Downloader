from pytube import YouTube
import os

FORMAT = "mp4"  # mp4 for video, mp3 for audio
VIDEOS = [""]

def download(format, videos):
    if format == "mp4":
        folder_name = "videos"
    elif format == "mp3":
        folder_name = "audios"
    else:
        print("Invalid format. Choose mp4 or mp3")
        return

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    for video in videos:
        yt = YouTube(video)
        title = yt.title

        if format == "mp4":
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=folder_name, filename=title + ".mp4")
            print(f"Downloaded {title} as video.")

        elif format == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path=folder_name, filename=title + ".mp3")
            print(f"Downloaded {title} as audio.")

download(FORMAT, VIDEOS)
