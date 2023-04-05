import wget
from info_download import ALBUM_ART_SAVE_PATH


class Song:
    def __init__(self, title, artist, album, album_art, album_art_filename=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.album_art = album_art
        self.album_art_filename = album_art_filename

    def __str__(self):
        return f"OBJECT : {self.title}, {self.artist}, {self.album}"

    def download_album_art(self):
        try:
            print(f"Downloading album art for {self.title}")
            wget.download(self.album_art, out=f"{ALBUM_ART_SAVE_PATH}/{self.title}.jpg")
            print()
        except Exception as e:
            print("Error in downloading album art!")
            print(e)
