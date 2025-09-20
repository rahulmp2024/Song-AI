import tkinter as tk
from yt_autoplay import play_youtube

def play_song():
    song=entry_song.get()
    platform=entry_platform.get()

    if platform.lower()=="youtube":
        status_label.config(text=f"-----playing {song} on YouTube -----")
        play_youtube(song)
    else:
        status_label.config(text="Platform not supported !!")

root=tk.Tk()
root.title("Song-AI Player")
root.geometry("400x250")


title=tk.Label(root,text="SONG - AI PLAYER ",font=("Arial",32,"bold"))
title.pack(pady=10)

song_label=tk.Label(root,text="Enter Song name: ")
song_label.pack()
entry_song=tk.Entry(root,width=50)
entry_song.pack(pady=5)

platform_label=tk.Label(root,text="Enter Platform (Youtube): ")
platform_label.pack()
entry_platform=tk.Entry(root,width=50)
entry_platform.pack(pady=5)

play_button=tk.Button(root,text="Play",command=play_song,bg="green",fg="white")
play_button.pack(pady=10)

status_label=tk.Label(root,text="",fg="blue",font=("Arial",12))
status_label.pack(pady=10)

root.mainloop()