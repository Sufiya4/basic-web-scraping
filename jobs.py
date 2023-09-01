from bs4 import BeautifulSoup 
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
#print(jobs[0])
file = open('jobsavailable.txt', 'w') 
for job in jobs:
    comp_name = job.find('h3', class_='joblist-comp-name').text.replace('','')
    skills = job.find('span', class_='srp-skills').text.replace(' ','')
    posted = job.find('span', class_='sim-posted').text
    #print(f"company name: {comp_name.strip()}\nskills req: {skills.strip()}\nposted: {posted.strip()}") 
    #print()
    file.write(f"company name: {comp_name.strip()}\nskills req: {skills.strip()}\nposted: {posted.strip()}")
    file.write("\n\n")
        
    

