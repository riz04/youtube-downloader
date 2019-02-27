import sys

from pytube import YouTube

# check if user has given url
try : 
    videoUrl = sys.argv[1]
    YouTube(videoUrl).streams.first().download()

except: 
    videoUrl = input("Provide URL :")
    print(videoUrl)

    YouTube(videoUrl).streams.first().download()