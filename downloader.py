from pytube import YouTube

videoUrl = input("enter video link : ")

print(videoUrl)

YouTube(videoUrl).streams.first().download()

