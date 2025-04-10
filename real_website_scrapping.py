from bs4 import BeautifulSoup
import requests

url = 'https://m.timesjobs.com/mobile/jobs-search-result.html?jobsSearchCriteria=Information%20Technology&cboPresFuncArea=35'
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li')

for job in jobs:
    post_time = job.find('span', class_='posting-time')
    if post_time:
        if post_time.text.strip() != '24h':
            continue
    else:
        continue  # Skip if posting time isn't found

    h3_tag = job.find('h3')
    if h3_tag:
        a_tag = h3_tag.find('a')
        if a_tag:
            job_name = a_tag.text.strip()
            print(f'Job name : {job_name}')
        else:
            continue

    skills_req = job.find_all(class_='srphglt')
    if skills_req:
        print('Skills Req : ', end='')
        for skill in skills_req:
            print(skill.text.strip(), end=', ')
        print()
    else:
        print("Skills Req : Not mentioned")

    print()
