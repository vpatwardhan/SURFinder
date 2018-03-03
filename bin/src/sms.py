# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 03:29:50 2018

@author: sguenov
"""

#from twilio.rest import Client
from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas
page = requests.get('http://announcements.surf.caltech.edu/')
data = page.text
soup = BeautifulSoup(data, "lxml")
table = soup.find_all('table')[2]

rows = table.find_all('tr')[3:]
data = {
    'titles' : [],
    'disiplines' : [],
    'mentor' : [],
    'posted' : []
}
for row in rows:
    print("row")
    cols = row.find_all('td')
    for col in cols:
        print("column ", col.text.strip())
    try:
        data['posted'].append( cols[3].text.strip() )
        data['titles'].append(cols[0].text.strip())
        data['disiplines'].append( cols[1].text.strip())
        data['mentor'].append(cols[2].text.strip())
        
    except:
        print("too short")
for key in data:
    print(key, data.get(key))
surfs = pandas.DataFrame(data)
surfs.to_csv("mySURFS.csv")
# # put your own credentials here
# account_sid = "AC5ef872f6da5a21de157d80997a64bd33"
# auth_token = "your_auth_token"
# client = Client(account_sid, auth_token)
# client.messages.create(  to="+16518675309",  from_="+14158141829", \
#                        body="Tomorrow's forecast in Financial District, \
#                        San Francisco is Clear",  \
#                        media_url="https://climacons.herokuapp.com/clear.png")