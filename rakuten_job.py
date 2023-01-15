import sys
import requests
from bs4 import BeautifulSoup

query = str(sys.argv[1])
url = 'https://japan-job-en.rakuten.careers/search-jobs?k='+ query
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
jobs_list = soup.find_all('li')
for job in jobs_list: 
    job_title = job.find('h2')
    if job_title:
        job_link = job.find('a').get("href")
        position = job_title.text
        print(f"Position: {position}")
        print(f"Link: {job_link}", end="\n\n\n")
        