import psycopg2
import requests
from bs4 import BeautifulSoup
"""
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(id="ResultsContainer")

job_res = results.find_all("div",class_="card-content")
for job_element in job_res:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
    #this is to print all the jobs listed on that webpage"""
db_name = 'scrapper'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'database'
db_port = '5432'
        
# This will create the connection the to postgres database.
conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)
        
        
def insert_into_table(job_title, company, loc):
    # This function will add the entry to database
    sql = """INSERT INTO bsDJango_data (job_title, company,loc) VALUES (%s, %s, %s)"""
            
    with conn:
        with conn.cursor() as curs:
            curs.execute(sql, (job_title, company, loc))
        
        
def truncate_table():
    # This function will delete the existing entries from the database.
    with conn:
        with conn.cursor() as curs:
            curs.execute("TRUNCATE scrapper CASCADE;")

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(id="ResultsContainer")

job_res = results.find_all("h2",string=lambda text: "python" in text.lower())
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in job_res
]
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    links = job_element.find_all("a")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    insert_into_table(title_element.text.strip(), company_element.text.strip(), location_element.text.strip())
    for link in links:
        if not link['href']=="https://www.realpython.com":
            link_url=link['href']
            print(f"Apply here: {link_url}\n")
    print()
    
