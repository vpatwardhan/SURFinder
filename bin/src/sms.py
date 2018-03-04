# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 03:29:50 2018

@author: sguenov
"""

from twilio.rest import Client
from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas
import os
import databaseFunctions
def checkSite():
    if os.path.exists("mySURFS.csv"):
        os.remove("mySURFS.csv")
    page = requests.get('http://announcements.surf.caltech.edu/')
    data = page.text
    soup = BeautifulSoup(data, "lxml")
    table = soup.find_all('table')[2]

    rows = table.find_all('tr')[7:]
    data = {
        'Project Title' : [],
        'Disiplines' : [],
        'Mentor' : [],
        'Posted' : []
    }
    for row in rows:
        cols = row.find_all('td')
        # for col in cols:
        #     print("column ", col.text.strip())
        try:
            data['Posted'].append(cols[3].text.strip())
            data['Project Title'].append(cols[0].text.strip())
            data['Disiplines'].append(str(cols[1].text.strip()))
            data['Mentor'].append(str(cols[2].text.strip()))
            
        except:
            pass

    surfs = pandas.DataFrame(data)
    surfs.to_csv("mySURFS.csv")
def sendTexts():
    message = ""
# # put your own credentials here
    account_sid = "ACf3099e9dbb87279fbc7fd3af79d78904"
    auth_token = "df0bd7d5a19f92c2f29a67d854d6d08f"
    client = Client(account_sid, auth_token)
    nums = databaseFunctions.getAllPhones()
    for num in nums:
        
        lst = databaseFunctions.getNewOpportunites(num)
        message += "There are new oppurtunities that matches your criteria. "
        for ide in lst:
            message += "The SURF is with Dr. " 
            message += databaseFunctions.getOppProfName(ide)
            message += "The project is "
            message += databaseFunctions.getOppTitle(ide)
            message += "Further information can be accessed at "
            message += databaseFunctions.getOppURL(ide)
            message += '\n'
        client.messages.create(num,
        body=message,
        from_="+12103616715")
def register():
    pass
if __name__ == "__main__":
    checkSite()