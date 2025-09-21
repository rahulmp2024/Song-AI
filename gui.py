import tkinter as tk
from yt_autoplay import play_youtube
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
from tkinter import ttk
import speech_recognition as sr


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="b30b11cec6874a8aba67403743f7e8fe",
    client_secret="541b8e8772b64d13bbc4c217c6422b8c",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-currently-playing",
    cache_path=".spotify_cache"
))


def play_spotify(song):
    results = sp.search(q=song, limit=1, type="track")
    items = results['tracks']['items']
    if items:
        track = items[0]
        status_label.config(text=f"-----Playing {track['name']} by {track['artists'][0]['name']} on Spotify -----")
        webbrowser.open(track['external_urls']['spotify'])
        return True
    return False

def play_song(song=None,platform=None):
    if song is None:
        song = entry_song.get().strip()
    if platform is None:
        platform = selected_platform.get()

    if not song:
        status_label.config(text="Please enter a song name!")
        return
    
    platform_lower = platform.lower()


    if platform_lower == "youtube":
        status_label.config(text=f"-----Playing {song} on YouTube -----")
        play_youtube(song)
    elif platform_lower == "spotify":
        if not play_spotify(song):
            status_label.config(text=f"Song not found on Spotify. Trying YouTube...")
            play_youtube(song)
    else:
        status_label.config(text="Platform not supported! Choose YouTube or Spotify.")

root = tk.Tk()
root.title("Song-AI Player")
root.geometry("450x300")

title = tk.Label(root, text="SONG - AI PLAYER", font=("Arial", 24, "bold"))
title.pack(pady=10)

song_label = tk.Label(root, text="Enter Song name:")
song_label.pack()
entry_song = tk.Entry(root, width=50)
entry_song.pack(pady=10)

platforms= ["YouTube","Spotify"]
selected_platform=tk.StringVar()
selected_platform.set(platforms[0])

platform_label = tk.Label(root, text="Choose Platform ")
platform_label.pack()
platform_dropdown=ttk.Combobox(root,values=platforms,textvariable=selected_platform)
platform_dropdown.current(0)
platform_dropdown.pack(pady=1)


status_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
status_label.pack(pady=10)

def get_voice_input(prompt="Say something : "):
    recognizer=sr.Recognizer()
    mic=sr.Microphone()

    status_label.config(text=prompt)
    root.update()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text=recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        status_label.config(text="Couldn't Understand")
        return ""
    except sr.RequestError:
        status_label.config(text="Speech Recognition Service failed !")
        return " "

def voice_play_process():
    song=get_voice_input("Yo Which song you want blud??")
    if not song:
        status_label.config(text="No song detected")
        return
    entry_song.delete(0,tk.END)
    entry_song.insert(0,song)


    platform = get_voice_input("Which Platform you want blud??")
    if not platform:
        platform="YouTube"

    platform_lower = platform.lower()
    if "spotify" in platform_lower:
        platform = "Spotify"
    elif "youtube" in platform_lower:
        platform = "YouTube"
    else:
        platform = "YouTube"

    selected_platform.set(platform)

    play_song(song,platform)
        
voice_song_button = tk.Button(root,text = "Tell your Song",command=voice_play_process)
voice_song_button.pack(pady=5)

play_button = tk.Button(root, text="Play", command=play_song, bg="green", fg="white")
play_button.pack(pady=10)




root.mainloop()
