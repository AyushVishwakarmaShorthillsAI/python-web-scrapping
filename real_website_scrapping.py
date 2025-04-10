from bs4 import BeautifulSoup
import requests
import time

url = 'https://m.timesjobs.com/mobile/jobs-search-result.html?jobsSearchCriteria=Information%20Technology&cboPresFuncArea=35'
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li')


def find_jobs():
    print('Enter the skill you are proficient in : ')
    skills_familiar = input('>').strip().lower()
    print(f'Filtering out for : {skills_familiar}\n')

    for job in jobs:
        post_time = job.find('span', class_='posting-time')
        if not post_time or post_time.text.strip() != '24h':
            continue

        h3_tag = job.find('h3')
        job_name = h3_tag.find('a').text.strip() if h3_tag and h3_tag.find('a') else "Not Found"

        skills_req = job.find_all(class_='srphglt')
        skill_texts = [skill.text.strip().lower() for skill in skills_req]

        if skills_familiar in skill_texts:
            print(f'Job Name : {job_name}')
            print('Skills Req : ', end='')
            for skill in skills_req:
                print(skill.text.strip(), end=', ')
            print()
            print()

if __name__=='__main__':
    while True:
        find_jobs()
        print('Wait for 2 second :)')
        time.sleep(2)

# NOTE : we can get inside the link of <a> tag and go to a new page and scrap the info present there
# to get to the link of href, use : ** 'a['href'] -> will give u the clickable link **
# Eg. : getting the job description from the link is possible by requresting the url and then scarapping it "