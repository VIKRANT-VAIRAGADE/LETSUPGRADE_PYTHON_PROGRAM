from pytube import YouTube

link = input("enter the link of video to download in lowest resolution : ")

yt = YouTube(link)
video = yt.streams.get_lowest_resolution()


video.download(" ")
print("downloaded")