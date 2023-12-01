import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# API client library
import googleapiclient.discovery
from moviepy.editor import AudioFileClip
from config import youtube_key
from pytube import YouTube

SONG_SAVE_PATH = "music-files"


def api_call(youtube, song_name):
    try:
        request = youtube.search().list(part="id,snippet", q=song_name)
        # Query execution
        response = request.execute()
    except Exception as E:
        print(E)

    # print(json.dumps(response, indent=4))
    return response


def get_video_ids(response):
    video_ids = []
    # print(response["items"])
    for i, item in enumerate(response["items"]):
        # print(item["id"])
        video_ids.append(item["id"]["videoId"])

    return video_ids


def download_song(song_name, video_id):
    # link of the video to be downloaded
    link = f"https://www.youtube.com/watch?v={video_id}"

    # make yt object
    try:
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    except Exception as e:
        print("Connection Error")
        print(e)

    try:
        print(f"{yt.title}, Length: {yt.length}s, Views: {yt.views:_}")
    except Exception as e:
        print(yt)

    # make audio_file
    audio_mp4 = yt.streams.filter(only_audio=True).first()
    # if file doesn't exist then download
    if not os.path.exists(f"{SONG_SAVE_PATH}/{song_name}.mp3"):
        print(f"Downloading {yt.title}")
        out_file = audio_mp4.download(
            output_path=SONG_SAVE_PATH, filename=song_name.title()
        )
    else:
        print(f"{yt.title} already exists!")
        return None

    # return name of the downloaded file
    return out_file


def select_song_to_download(video_ids):
    # just download the first song
    return video_ids[0]


def convert_file(out_file):
    # split filename and extension
    base, ext = os.path.splitext(out_file)
    audio_mp4_file = AudioFileClip(out_file)
    # convert mp4 to mp3
    print("Converting to mp3")
    audio_mp4_file.write_audiofile(base + ".mp3")
    # delete the prev mp4 file
    os.remove(out_file)


def api_information():
    # API information
    api_service_name = "youtube"
    api_version = "v3"
    # API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=youtube_key
    )
    return youtube


def download(song_name):
    """
    path_to_chromedriver = "C:\\Users\\hhsud\\Downloads\\chromedriver.exe"
    # driver = webdriver.Chrome(path_to_chromedriver)
    driver = webdriver.Chrome()
    driver.maximize_window()
    website_url = "https://free-mp3-download.net/"
    driver.get(website_url)
    # search box 
    """
    youtube = api_information()
    response = api_call(youtube, song_name)
    video_ids = get_video_ids(response)

    video_id = select_song_to_download(video_ids)
    out_file = download_song(song_name, video_id)
    if out_file:
        convert_file(out_file)
        return 1
    else:
        return 0
