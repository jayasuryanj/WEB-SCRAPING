from selenium import webdriver
import requests as rq
import os
from bs4 import beatifulsoap
import time

path = input("enter path : ")
url = input("enter url: ")
output = "output"
def get_url(path, url):
	driver = webdriver.chrome(executable_path=r"{}".format(path))
	driver.get(url)
	print("loading. . . ..")
	res driver.execute_script("return document.document.Element.outerHTML")

	return res

	def get_img_links(res):
		soup = beatifulsoap(res, "lxml")
		imglinks = soup.find_all("img", src=True)
		return getlinks
def download_img(img_link, index):
	try:
		extensions = [".jpeg", ".png", ".gif"]
		extensions = ".jpg"
		for exe in extensions:
			if img_link.find(exe > 0:
				extension = exe
				break 
		img_data = rq.get(img_link.content
		with open(output + "\\" + str(index + 1) + extension, "web+") as f:
			f.write(img_data)
		f.close()
	except Exception:
		pass

result = get_url(path, url)
time.sleep(60)
img_links = get_img_links(result)
if not os.path.isdir(output);
    os.mkdir(output)
for index, img_link in enumerate(img_links):
	img_link = img_link["src"]
	print("downloading...")
	if img_link:
		download_img(img_link, index)
print("download complete!")

