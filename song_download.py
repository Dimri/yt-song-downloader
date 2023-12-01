import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Set the download folder in the preferences
SONG_SAVE_PATH = "D:\\Projects\\yt-song-downloader\\music-files"
prefs = {
    "download.default_directory": SONG_SAVE_PATH,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options)

def download(song_name, auto_download=True):
    website_url = "https://free-mp3-download.net/"
    driver.get(website_url)
    # search box
    search_box = driver.find_element(By.ID, "q")
    search_btn = driver.find_element(By.ID, "snd")
    time.sleep(2)
    search_box.send_keys(song_name)
    search_btn.click()
    time.sleep(5)
    # TODO: wait for results to load if results not found then put the song name in a separate list
    table = driver.find_element(By.ID, "results_t")
    rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    
    if auto_download == False:
        print(f"  {'Title':50}\t{'Duration':5}")
        print("#" * 80)
        min_len = min(len(rows), 5)
        for i, row in enumerate(rows[:min_len]):
            col = row.find_elements(By.TAG_NAME, "td")
            print(f"{i+1}. {col[0].text:50}\t{col[1].text:5}")
        # song_num = int(input("\nSelect the song number to download. "))
        song_num = 1
        assert song_num >= 1 and song_num <= min_len, "please enter a correct number"
    else:
        song_num = 1

    download_btn = rows[song_num-1].find_elements(By.TAG_NAME, "td")[2]
    download_link = download_btn.find_element(By.TAG_NAME, "a")
    download_link.click()
    time.sleep(5)
    # new page
    btn = driver.find_element(By.TAG_NAME, "button")
    btn.click()
