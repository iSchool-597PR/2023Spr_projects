from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
job_title = 'software developer'
location = 'united states'

base_url = 'https://monster.com/jobs'
params = {'q': job_title, 'where': location, 'page': '1', 'so': 'm.s.sh'}
search_url = base_url + '/search?'
en_url = search_url + urllib.parse.urlencode(params)
print(en_url)

driver.get(base_url)

job_role = driver.find_element(By.XPATH, '//input[@id="search-job"]')
job_role.clear()
job_role.send_keys('software developer')
location = driver.find_element(By.XPATH, '//input[@id="search-location"]')
location.clear()
location.send_keys('united states')
search = driver.find_element(By.XPATH, '//button[@class="btn btn-purple-fill"]')
search.click()

html = driver.find_element(By.TAG_NAME, 'html')
soup = BeautifulSoup(html.get_attribute('innerHTML'), 'html.parser')
print(soup.prettify())
# print(soup.find_all('div', attrs={'class': "job-search-resultsstyle_LoadMoreContainer-sc-1wp+60K-1"}))

# jobs = driver.find_elements(By.XPATH, '//a[@class="job-cardstyle__JobCardTitle-sc-1mbmxes-2 iQztVR"]')
# for i in jobs:
#     print(i.get_attribute('innerHTML'))
# jobs[0].click()

# jobs = driver.find_elements((By.XPATH, '//div[contains(@class, "job-cardstyle__JobCardComponent-sc-1mbmxes-0")]/a'))
# for i in jobs:
#     print(i)

jobs = driver.find_elements(By.XPATH, '//div[contains(@class, "job-cardstyle__JobCardComponent-sc-1mbmxes-0")]//descendant::a')
for i in jobs:
    print(i.get_attribute('href'))
    print(i.get_attribute('innerHTML'))
print(jobs[0])
jobs[0].click()

load_more = driver.find_element(By.XPATH, '//div[@class="job-search-resultsstyle__LoadMoreContainer-sc-1wpt60k-1 bEEwpP"]')
print(load_more.get_attribute('innerHTML'))
# load_more.click()

# job_desc = driver.find_element(By.XPATH, '//div[@tabindex="0"]')
# print(job_desc.get_attribute('innerHTML'))

url_list = []

# while len(url_list) < 10:
#     curr_url = driver.current_url
#     wait = WebDriverWait(driver, 20)
#     urls = wait.until(EC.presence_of_all_elements_located(
#         (By.TAG_NAME, 'a')))
#     # urls = driver.find_elements(By.TAG_NAME, 'a')
#     # urls = driver.find_elements(By.XPATH, '//a[@class="job-cardstyle_JobCardTitle-sc-1mbmxes-2 iQztVR"]')
#     print(urls)
#     for i in urls:
#         print(i.get_attribute('href'))
#         url_list.append(i.get_attribute('href'))


time.sleep(60)
# print(url_list)

driver.close()
