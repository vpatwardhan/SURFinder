# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 03:29:50 2018

@author: sguenov
"""

from twilio.rest import Client
from lxml import html
import requests
page = requests.get('http://announcements.surf.caltech.edu/')
tree = html.fromstring(page.content)
titles =  tree.xpath('//div[@title="buyer-name"]/text()')

# put your own credentials here
account_sid = "AC5ef872f6da5a21de157d80997a64bd33"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)
client.messages.create(  to="+16518675309",  from_="+14158141829", \
                       body="Tomorrow's forecast in Financial District, \
                       San Francisco is Clear",  \
                       media_url="https://climacons.herokuapp.com/clear.png")