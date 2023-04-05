import music_tag
from song import Song
from info_download import song_info
from info_download import ALBUM_ART_SAVE_PATH
from song_download import SONG_SAVE_PATH


def set_song_attrs(file, song_obj):
    file["title"] = song_obj.title
    file["artist"] = song_obj.artist
    file["album"] = song_obj.album
    # file["year"] = song_obj.
    file["artwork"] = get_artwork(song_obj)
    return file


def get_artwork(song_obj):
    try:
        with open(
            f"{ALBUM_ART_SAVE_PATH}/{song_obj.album_art_filename}", "rb"
        ) as img_in:
            return img_in.read()
    except Exception as e:
        print("Error loading album art")
        print(e)


def change_metadata(song, song_obj):
    try:
        file = music_tag.load_file(f"{SONG_SAVE_PATH}/{song}.mp3")
    except Exception as e:
        print("Error loading file")
        print(e)
        return
    file = set_song_attrs(file, song_obj)
    file.save()
