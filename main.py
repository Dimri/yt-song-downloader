import time
import fileinput
from pathlib import Path
from song_download import download
from info_download import song_info
from metadata import change_metadata


def get_song_info(song):
    print("\nGetting song information!")
    song_obj = song_info(song)
    return song_obj


def set_music_metadata(song, song_obj):
    print(f"\nChanging metadata for song : {song_obj.title}")
    change_metadata(song, song_obj)


def main():
    time.sleep(10)
    for song in fileinput.input():
        song = song.replace("\n", "").replace(".mp3", "")
        print(f"query: {song}")
        download(song, auto_download=False)
        # if download_song(song, auto_download=False):
        #     song_obj = get_song_info(song)
        #     set_music_metadata(song, song_obj)
        print("*" * 50)


if __name__ == "__main__":
    main()
