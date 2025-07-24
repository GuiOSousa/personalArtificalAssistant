import subprocess
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

class Spotify():
    def __init__(self):
        load_dotenv()
    
    def getAuth(self, scope: str):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.environ.get("SPOTIFY_ID"),
            client_secret=os.environ.get("SPOTIFY_SECRET"),
            redirect_uri=os.environ.get("SPOTIFY_REDIRECT"),
            scope=scope
        ))

        devices = sp.devices()
        if len(devices["devices"]) == 0:
            self.openSpotify(sp)
            
        return sp

    def openSpotify(self, sp):
        subprocess.Popen("Spotify.exe")
        time.sleep(5)
        devices = sp.devices()
        deviceId = devices["devices"][0]["id"]
        sp.transfer_playback(deviceId, force_play=True)
        

    def getSongURI(self, songTitle: str):
        sp = self.getAuth('user-read-playback-state user-modify-playback-state')
        results = sp.search(q=songTitle, type='track', limit=1)

        uri = results['tracks']['items'][0]['uri']
        return uri

    def getSavedSongs(self):
        sp = self.getAuth('user-library-read')
        savedSongs = []
        results = sp.current_user_saved_tracks()
        for item in enumerate(results['items']):
            track = item['track']
            savedSongs.append(track)
        return savedSongs
    
    def playSong(self, songTitle: str):
        sp = self.getAuth('user-read-playback-state user-modify-playback-state')
        songURI = self.getSongURI(songTitle)

        sp.start_playback(uris=[songURI])
    
    def addSongToQueue(self, songTitle: str):
        sp = self.getAuth('user-read-playback-state user-modify-playback-state')
        songURI = self.getSongURI(songTitle)

        sp.add_to_queue(songURI)
    
    def pauseSong(self):
        sp = self.getAuth('user-modify-playback-state')
        sp.pause_playback()
    
    def resumeSong(self):
        sp = self.getAuth('user-modify-playback-state')
        sp.start_playback()
