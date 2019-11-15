from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import collections
import time
import csv


# while True:
#     try:
#         loadMoreButton = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[4]/nba-stat-table/div[2]/div/a")
#         time.sleep(2)
#         loadMoreButton.click()
#         time.sleep(5)
#     except Exception as e:
#         print(e)
#         break
# print("Complete")
# time.sleep(10)

def getListingLinks(link):
# Open the driver
	driver = webdriver.Chrome()
	driver.get(link)

# Save the links
	craig_title = []
	all_posts = driver.find_elements_by_class_name("result-row")
	for post in all_posts:
		craig_title.append(post.text)

	driver.close()
	print(craig_title)

getListingLinks('https://sfbay.craigslist.org/search/sso')
# header_list = []

# table_headers = driver.find_element_by_xpath('/html/body/section/form/div[4]/ul')
# # headers = table_headers.find_elements_by_tag_name('/html/body/section/form/div[4]/ul/li')

# for row in table_headers:
# 	header_col = row.find_elements_by_tag_name('li')
# 	for item in header_col: 
# 		t = item.text
# 		header_list.append(t)
# 		# print(t)

# print(header_list)

# csv_file = open('craigslist.csv', 'w', newline='')
# writer = csv.writer(csv_file)
# writer.writerow(header_list)
# csv_file.close()

####	

# table_body = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/nba-stat-table/div[1]/div[1]/table/tbody')
# body_row = table_body.find_elements_by_tag_name('tr')

# for cell in body_row:
# 	cell_list_text = []
# 	cell_list = cell.find_elements_by_tag_name('td')
# 	for item in cell_list:
#  		t = item.text
#  		cell_list_text.append(t)

# 	with open('nbaplayerstats1.csv', 'a', newline='') as f:
#  		writer = csv.writer(f)
#  		writer.writerow(cell_list_text)
#  		csv_file.close()
