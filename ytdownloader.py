from pytube import YouTube
from sys import argv

# grabbing video link from cmd by using argv
# argv - takes all the things from input (cmd)
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download("/Users/hbish/Desktop/Movies/ytdownloader/")