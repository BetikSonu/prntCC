from selenium import webdriver
import random
import string
import warnings
warnings.filterwarnings('ignore')


def twostr(stringLength=2):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))


def forint(intLength=4):
	for i in range(4):
		return str(random.randint(1000, 9999))


def imgRead():
	return open("sc.png", "r")


brwsr = webdriver.PhantomJS("./phantomjs.exe")
while True:
	start = twostr()
	finish = forint()
	brwsr.get("https://prnt.sc/" + start + finish)
	link = brwsr.find_element_by_xpath('//*[@id="screenshot-image"]').get_attribute("src")
	brwsr.get(link)
	if brwsr.get_screenshot_as_png() == imgRead():
		pass
	else:
		brwsr.save_screenshot("img/" + start + finish + ".png")
		print("Created File: "+start+finish+".png")
