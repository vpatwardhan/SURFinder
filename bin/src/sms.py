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
            data['Disiplines'].append( cols[1].text.strip())
            data['Mentor'].append(cols[2].text.strip())
            
        except:
            print("too short")

    surfs = pandas.DataFrame(data)
    surfs.to_csv("mySURFS.csv")
def sendTexts():
    message = ""
# # put your own credentials here
    account_sid = "PN0a19970c38e1a1d72c155dd5a38efde3"
    auth_token = "df0bd7d5a19f92c2f29a67d854d6d08f"
    client = Client(account_sid, auth_token)
    nums = databaseFunctions.getAllPhones()
    for num in nums:
        message += "There is a new oppurtunity that matches your criteria. "
        lst = databaseFunctions.getNewOpportunites(num)
        for ide in lst:
            message += "It is with Dr. " 
            message += databaseFunctions.getOppProfName(ide)
            message += "The project is "
            message += databaseFunctions.getOppTitle(ide)
            message += "Further information can be accessed at"
            message += databaseFunctions.getOppURL(ide)
    client.messages.create(message)
def register():
    pass
if __name__ == "__main__":
    checkSite()