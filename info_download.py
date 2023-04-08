import requests
import json
import os

ALBUM_ART_SAVE_PATH = "album-arts"
from config import rapidapi_header
from song import Song


def change_title(song):
    song = song.replace("?", "")
    song = song.replace('"', "")
    return song


def get_response_obj(song_name):
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    querystring = {"q": song_name}
    headers = rapidapi_header
    response = requests.request("GET", url, headers=headers, params=querystring)
    assert response.status_code == 200, f"{response.status_code}. Error!"
    response_json = json.loads(response.text)
    return response_json


def make_song_obj(result):
    song_obj = Song(
        title=change_title(result["title"]),
        artist=result["artist"]["name"],
        album=result["album"]["title"],
        album_art=result["album"]["cover_big"],
    )
    song_obj.album_art_filename = f"{song_obj.title}.jpg"
    return song_obj


def song_info(song_name):
    response = get_response_obj(song_name)
    result = response["data"][0]
    song_obj = make_song_obj(result)
    if not os.path.exists(f"{ALBUM_ART_SAVE_PATH}/{song_obj.album_art_filename}"):
        song_obj.download_album_art()
    else:
        print(f"Album art already downloaded for the song : {song_obj.title}")
    return song_obj
