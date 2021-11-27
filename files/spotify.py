import spotipy, json
from spotipy.oauth2 import SpotifyOAuth

class spotifyController:
    def __init__(self) -> None:
        with open("config.json") as f:
            config = json.load(f)

        self.paused = False
        self.clientId = config["spotifyCreds"]["spotifyClientId"]
        self.clientSecret = config["spotifyCreds"]["spotifyClientSecret"]
        self.s = s = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.clientId, client_secret=self.clientSecret, redirect_uri="http://localhost:8081", scope="user-modify-playback-state"))
    
    def nextTrack(self):
        self.s.next_track()
    
    def previousTrack(self):
        self.s.previous_track()
    
    def changeVolume(self, percent):
        if int(percent) > 100:
            pass
        if int(percent) < 0:
            pass
        else:
            self.s.volume(percent)

    def pause(self):
        if self.paused != True:
            self.s.pause_playback()
            self.paused = not self.paused
            return
        self.s.start_playback()
        self.paused = not self.paused
        return
