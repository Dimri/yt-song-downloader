import fileinput
import os
from song_download import download
from info_download import song_info
from metadata import change_metadata


def download_song(song):
    flag = download(song)
    if flag:
        print("Download completed")
        print("\n" * 3)


def get_song_info(song):
    print("\nGetting song information!")
    song_obj = song_info(song)
    return song_obj


def set_music_metadata(song, song_obj):
    print(f"\nChanging metadata for song : {song_obj.title}")
    change_metadata(song, song_obj)


def main():
    for song in fileinput.input():
        song = song.replace("\n", "")
        print(f"query: {song}")
        download_song(song)
        song_obj = get_song_info(song)
        set_music_metadata(song, song_obj)
        print("DONE\n")
        break


if __name__ == "__main__":
    main()
