
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time

def play_youtube(song_name):
    service = Service(r"C:\Users\pheno\OneDrive\Projects\SongAI\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://www.youtube.com")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(song_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    

    video = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "video-title"))
    )
    video.click()
    time.sleep(2)
    driver.refresh()


    print(f"Now Playing {song_name} on YouTube via Edge")
    input("Press Enter to close browser...")
    driver.quit()



