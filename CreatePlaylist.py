import requests
import json
from secrets import secrets
import os

class CreatePlaylist:
    def __init__(self):
        pass

    def getYoutubeClient(self):
        pass

    def getLikedVideos(self):
        pass

    def createPlaylist(self):
        requestBody = json.dumps({
            "name": "YouPyPlaylist",
            "description": "Auto youtube to spotify playlist",
            "public": True
        })
        query = "https://api.spotify.com/v1/users/{}/playlists".format(secrets["userIDSpotify"])
        print("query*****: "+str(query))
        response = requests.post(
            query,
            data=requestBody,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(secrets["spotifyToken"])
            }
        )
        response_json = response.json()
        print("response*****: "+str(response_json))
        return response_json["id"]

    def getSpotifyUri(self, song_name, artist):
        # reihenfolge wichtig..... track => artist ???wtf
        query="https://api.spotify.com/v1/search?q=track%3A{}%20artist%3A{}&type=track".format(
            song_name,
            artist
        )
        response= requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(secrets["spotifyToken"])
            }
        )
        response_json= response.json()

        songs= response_json["tracks"]["items"]
        print("songs****: "+str(songs))
        uri= songs[0]["uri"]
        print("uri*****:  "+str(uri))
        return uri

    def addSongToPlaylist(self):
        pass


test = CreatePlaylist()
CreatePlaylist.getSpotifyUri(test,"semmelweisreflex", "fatoni")
