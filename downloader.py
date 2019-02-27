import sys

from pytube import YouTube

videoUrl = sys.argv[1]

print(videoUrl)

YouTube(videoUrl).streams.first().download()