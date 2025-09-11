from yt_autoplay import play_youtube

def play_song(song,platform):
    if platform.lower() == 'youtube':
        play_youtube(song)
    else:
        print("Platform not supported")


song=input("Enter song name : ")
platform=input("Which platform - ")
play_song(song,platform)