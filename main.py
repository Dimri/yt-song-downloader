import fileinput
from song_download import download


if __name__ == "__main__":
    for song in fileinput.input():
        song = song.split(".mp3")[0]
        print(f"query: {song}")
        download(song, auto_download=False)
        print("*" * 50)
