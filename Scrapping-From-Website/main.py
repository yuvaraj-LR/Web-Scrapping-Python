from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')

print("Select the skill that you are not familiar with")
unfamiliar_Skills = input('>')
print(f'Filtering out {unfamiliar_Skills}')

def find_jobs():
    jobs_List = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    count=0
    for job in jobs_List:
        time = job.find('span', class_='sim-posted').text

        # Check the condition if the job are posted few days.
        if ('few days' in time):
        
            company_Name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            company_Name = company_Name.strip()
            skills = skills.strip()
            job_details = job.header.h2.a['href']

            # Filtering the result by removing with unfamiliar skills.
            if unfamiliar_Skills not in skills:
                count += 1
                with open("test.txt", 'a') as f:
                    f.write(f"Company Name:  {company_Name} \n")
                    f.write(f"Skills Required:  {skills} \n")
                    f.write(f"For More Details:  {job_details}\n \n")
    return count    

if __name__ == '__main__':
    count = find_jobs()
    print(f"{count} Jobs Found!!!")
    print("Done")
