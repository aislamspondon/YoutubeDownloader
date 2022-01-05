from tkinter.constants import Y
from pytube import YouTube
url = "https://www.youtube.com/watch?v=hLlDSC8NVGY"
video_url = YouTube(str(url))
videos = video_url.streams.first()
videos.download()