from yt_autoplay import play_youtube
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="b30b11cec6874a8aba67403743f7e8fe",
    client_secret="541b8e8772b64d13bbc4c217c6422b8c",
    redirect_uri="http://127.0.0.1:8888/callback",
    cache_path=".spotify_cache"
))




    
def play_spotify(song):
    
    results = sp.search(q=song, limit=1, type="track")
    items = results['tracks']['items']
    if items:
        track = items[0]
        print("Found on Spotify:", track['name'], "by", track['artists'][0]['name'])
        webbrowser.open(track['external_urls']['spotify'])
        return True
    return False



def play_song(song, platform):
    platform = platform.lower().strip()
    if platform == 'youtube':
        play_youtube(song)
    elif platform == 'spotify':
        if not play_spotify(song):
            print("Song not found on Spotify. Falling back to YouTube...")
            play_youtube(song)
    else:
        print("Platform not supported. Choose YouTube or Spotify.")


song=input("Enter song name : ")
platform=input("Which platform (YouTube/Spotify) -  ")
play_song(song,platform)