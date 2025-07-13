from pytube import YouTube

url = input("Enter Youtube URL: ")
yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

stream.download()
print("download is completed")