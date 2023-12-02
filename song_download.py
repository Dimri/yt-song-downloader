import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

SONG_SAVE_PATH = "D:\\Projects\\yt-song-downloader\\music-files"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
prefs = {
    "download.default_directory": SONG_SAVE_PATH,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_extension("adblocker.crx")
driver = webdriver.Chrome(chrome_options)

def check_if_temp_file_is_made():
    wait = True
    timeout = 10
    current_time = 0
    while wait and current_time <= timeout:
        time.sleep(1)
        music_dir = Path(SONG_SAVE_PATH)
        temp_file = list(music_dir.rglob("*.crdownload"))
        if len(temp_file):
            wait = False
        current_time += 1 
    return wait

def search_song(song_name):
    search_box = driver.find_element(By.ID, "q")
    search_btn = driver.find_element(By.ID, "snd")
    search_box.clear()
    search_box.send_keys(song_name)
    search_btn.click()
    time.sleep(2)

def check_exists_by_ID(id):
    try:
        driver.find_element(By.ID, id)
    except NoSuchElementException:
        return False
    return True

def search_song_and_check(song_name):
    search_song(song_name)
    if check_exists_by_ID("results_t"):
        table = driver.find_element(By.ID, "results_t")
        rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
        return rows
    else:
        return False

def show_options(rows):
    print(f"  {'Title':50}\t{'Duration':5}")
    print("#" * 80)
    min_len = min(len(rows), 5)
    for i, row in enumerate(rows[:min_len]):
        col = row.find_elements(By.TAG_NAME, "td")
        print(f"{i+1}. {col[0].text:50}\t{col[1].text:5}")
    try:
        song_num = int(input("\nSelect the song number to download. (Press anything else to skip the song).\t"))
    except ValueError:
        song_num = 0
    if song_num >= 1 and song_num <= min_len:
        return song_num
    else:
        return 0

def download(song_name, auto_download=True):
    website_url = "https://free-mp3-download.net/"
    driver.get(website_url)
    out = search_song_and_check(song_name)
    if out:
        rows = out
    else:
        print(f"Table not found! Retrying once")
        time.sleep(2)
        out_v2 = search_song_and_check(song_name)
        if out_v2:
            rows = out_v2
        else:
            print(f"{song_name} not found. Skipping!")
            return 0

    if auto_download == False:
        song_num = show_options(rows)
    else:
        song_num = 1

    if song_num == 0:
        print(f"Skipping")
        return 0

    download_btn = rows[song_num-1].find_elements(By.TAG_NAME, "td")[2]
    download_link = download_btn.find_element(By.TAG_NAME, "a")
    download_link.click()
    # wait to fill captcha
    input("Press enter after solving captcha!!")
    btn = driver.find_element(By.TAG_NAME, "button")
    btn.click()
    flag = check_if_temp_file_is_made()
    if flag:
        print("Request timed out!")
    return 1