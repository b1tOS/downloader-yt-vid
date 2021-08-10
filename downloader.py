import pytube

url = input('Paste youtube video link: ')

yt = pytube.YouTube(url)

aud = input('Video or audio? (v/a): ') == "a"

if aud:
    for audios in yt.streams.filter(only_audio=True):
        print("Type of stream:", audios)
else:
    for videos in yt.streams.filter(only_video=True):
        print("Type of stream:", videos)

itag = int(input("Select type of stream by itag: "))
stream = yt.streams.get_by_itag(itag)
stream.download()
print("Загрузка закончилась, имя файла: ", stream.title)
