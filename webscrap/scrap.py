import json
import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup
from os import environ as env
from pymongo import MongoClient

""""DataBase Connection"""
clinet = MongoClient(env['MONGO_URI'])
db = client.get_database('professor_db')
records = db.professor_records
print("Number of records: {}".format(records.count_documents({})))

"""Website Scraping"""
page = requests.get(env['URL'])
soup = BeautifulSoup(page.content,'html.parser')
professors_list = soup.findAll(attrs = {'id':'professors-contents'})
ls = professors_list[0].find_all('a')

"""Data preprocessing and cleaning"""
Dict = []
for x in ls:
  Dict.append([x.get_text(),x.get('href')])
  #print(x.get('href'),x.get_text())

def clean_data(val):
  if len(val) > 0:
    Val = val[0].get_text()
    Val = Val.replace('\n',' ')
    Val = Val.replace('\xa0',' ')
    Val = Val.strip()
    return Val
  return []


"""Send Data to database"""
for x in Dict:
  try:
    data = requests.get(x[1])
    soup = BeautifulSoup(data.content, 'html.parser')
    about = soup.findAll(attrs= {'class' : 'title-and-body-text'})
    About = clean_data(about)
    areas_of_expertise = soup.findAll(attrs= {'class': 'staff-profile-areas-of-expertise'})
    Area_of_expertise = clean_data(areas_of_expertise)
    career_highlights = soup.findAll(attrs= {'class': 'staff-profile-career-highlights',})
    Career =  clean_data(career_highlights)
    more_info = soup.findAll(attrs = {'class' : 'article-item expander-list'})
    More_info = clean_data(more_info)
    publications = soup.findAll(attrs= {'id': 'publications-contents'})
    Publications = clean_data(publications)
    supervision = soup.findAll(attrs= {'id':'supervision-contents'})
    Supervision = clean_data(supervision)
    career_history = soup.findAll(attrs= {'id':'career-history-contents'})
    Career_history = clean_data(career_history)
    affiliated_positions = soup.findAll(attrs={'id':'affiliated-positions-contents'})
    Affiliated_positions = clean_data(affiliated_positions)
    invited_presentations_lectures_and_conferences = soup.findAll(attrs={'id':"invited-presentations-lectures-and-conferences-contents"})
    Invited_presentations_lectures_and_conferences = clean_data(invited_presentations_lectures_and_conferences)
    taught_modules = soup.findAll(attrs={'id':'taught-modules-contents'})
    Taught_modules = clean_data(taught_modules)
    key_grants = soup.findAll(attrs={'id':'key-grants-and-projects-contents'})
    Key_grants_and_projects = clean_data(key_grants)
    public_engagements = soup.findAll(attrs={'id':'public-engagements-contents'})
    Public_engagements = clean_data(public_engagements)
    Professors = {x[0] : {'About':About,
                          'Area_of_expertise': Area_of_expertise,
                          'Career_highlights': Career,
                          'More_info': More_info,
                          'Publications':Publications,
                          'Supervision':Supervision,
                          'Career_history':Career_history,
                          'Affiliated_positions': Affiliated_positions,
                          'Invited_presentations_lectures_and_conferences' : Invited_presentations_lectures_and_conferences,
                          'Taught_modules':Taught_modules,
                          'Key_grants_and_projects':Key_grants_and_projects,
                          'Public_engagements':Public_engagements}}
    try : 
      records.insert_one(Professors)
    except:
      print("Some error in inserting data")
  except:
    print('Link Invalid')


print("Toatal no of records after data push: {}".format(records.count_documents({})))