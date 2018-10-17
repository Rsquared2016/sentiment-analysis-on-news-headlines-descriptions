from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import csv
import re

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

proxies = {
  'http': '103.206.132.201:56775',
  'https': '103.206.132.201:56775',
}

options.add_argument('--proxy-server=178.215.190.96:61028')


# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\VL21\Desktop\chromedriver_win32/chromedriver.exe')

driver.get("https://www.bloomberg.com/search?query=Wells+Fargo&endTime=2018-10-14T14:21:37.033Z&page=1")
time.sleep(3)
# Click review button to go to the review section

# Windows users need to open the file using 'w'
# csv_file = open('reviews.csv', 'w')
csv_file = open('jpmorganlinks.csv', 'w+')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
index = 1
while True:
	try:
		print("Scraping Page number " + str(index))
		index = index + 1
		# Find all the reviews on the page
		wait_article = WebDriverWait(driver, 10)
		articles = wait_article.until(EC.presence_of_all_elements_located((By.XPATH,
									'//h1[@class="search-result-story__headline"]')))
		time.sleep(3)
		for art in articles:
			# Initialize an empty dictionary for each review
			# Use relative xpath to locate the title, text, username, date.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			link = art.find_element_by_xpath('./a').get_attribute('href')
			writer.writerow(link)
			time.sleep(2)

		# Locate the next button on the page.
		wait_button = WebDriverWait(driver, 10)
		next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
									'//*[@id="content"]/div/section/section[2]/section[1]/div[5]/a')))
		next_button.click()
		time.sleep(5)
	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break
