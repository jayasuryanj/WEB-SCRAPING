from selenium import webdriver
import requests as rq
import os
from bs4 import BeautifulSoup
import time

path = input("Enter path: ")
url = input("Enter URL: ")
output = "output"

def get_url(path, url):
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    print("Loading...")
    time.sleep(5)  # Adjust the sleep duration as needed, ensuring the page loads before getting HTML
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()  # Close the webdriver

    return res

def get_img_links(res):
    soup = BeautifulSoup(res, "html.parser")
    img_links = soup.find_all("img", src=True)
    return img_links

def download_img(img_link, index):
    try:
        extensions = [".jpeg", ".png", ".gif", ".jpg"]  # List of image extensions
        extension = ""
        for exe in extensions:
            if img_link["src"].endswith(exe):
                extension = exe
                break
        if extension:
            img_data = rq.get(img_link["src"]).content
            with open(os.path.join(output, f"{index + 1}{extension}"), "wb") as f:
                f.write(img_data)
    except Exception as e:
        print(f"Failed to download image {index + 1}: {e}")

result = get_url(path, url)
img_links = get_img_links(result)
if not os.path.isdir(output):
    os.mkdir(output)

for index, img_link in enumerate(img_links):
    print(f"Downloading image {index + 1}...")
    download_img(img_link, index)

print("Download complete!")
