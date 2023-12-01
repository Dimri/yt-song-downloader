# yt-song-downloader
Script download Youtube videos as mp3. Then download the related music information and changed the music tags in the mp3 file.  
<br>
1. Download mp4 (only audio) file using YouTube api. 
2. Convert the mp4 file to mp3 using `moviepy`.
3. Download music information using Deezer api.
4. Using the above information change the music tags of the mp3 file using `music_tag` module.
<br>
Add a `config.py` file with rapidapi headers and your youtube api key. <br>



## Example

Run the code using `python main.py songs.txt`. In this example, `songs.txt` file the song :
1. Heat Waves - Glass Animals

---

Output : <br>
```
query: Heat Waves - Glass Animals
Glass Animals - Heat Waves (Official Video), Length: 235s, Views: 519_892_439
Downloading Glass Animals - Heat Waves (Official Video)
Converting to mp3
MoviePy - Writing audio in D:\Projects\yt-song-downloader\music-files\Heat Waves - Glass Animals.mp3
MoviePy - Done.
Download completed





Getting song information!
Downloading album art for Heat Waves


Changing metadata for song : Heat Waves
DONE
```

