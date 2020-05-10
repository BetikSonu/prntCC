import time
import urllib

from selenium import webdriver
import random
import string


def twostr(stringLength=2):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))


def forint(intLength=4):
	for i in range(4):
		return str(random.randint(1000, 9999))



brwsr = webdriver.Chrome()
while True:
	start = twostr()
	finish = forint()
	brwsr.get("https://prnt.sc/" + start + finish)
	link = brwsr.find_element_by_xpath('//*[@id="screenshot-image"]').get_attribute("src")
	brwsr.get(link)
	brwsr.save_screenshot(start + finish + ".png")
