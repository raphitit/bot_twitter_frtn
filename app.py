#!/usr/bin/env python

#Please do not change anything to this section!
import sys
import os
import time
from twython import Twython, TwythonError
from datetime import datetime
import pytz

CONSUMER_KEY = os.environ['k3AlA1eOKu1dQK3CLWx8aKl4Y']
CONSUMER_SECRET = os.environ['CPbATVVjbkn31BvPudOg32d5LVpPM42LUHOO1PUzBLKgDd87vs']
OAUTH_TOKEN = os.environ['1208145990626299905-KMtHIAcgOvRWXex8GFXPiBk2vKEkvV']
OAUTH_TOKEN_SECRET = os.environ['t7um49fZRaS4Ce21zvTAQ1GJTpdUiFNHm4eKRzou1VMXG']
TWEET_LENGTH = 280
TWEET_URL_LENGTH = 21
#Please so not change anything to this section!

today = datetime.now()
tz = pytz.timezone('Asia/Manila') # change the timezone to your desired/home timezone.
pht = datetime.now(tz) #change the variable too if you want

def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

photo = open('./output/shop.png', 'rb')

#Change the text into anything you like! (and please change the variables accordingly if you changed it above.)
tweetStr = 'Fortnite item shop for '+pht.strftime("%m/%d/%y")+'!\n'+pht.strftime("%I:%M %p")+', PHT/GMT+8\n\nIf you want to support me, make sure to use code \"KuletXCore\" on the Fortnite Item Shop!\nReally appreciate it!'

api = twitter_handle()
response = api.upload_media(media=photo)
api.update_status(status=tweetStr, media_ids=[response['media_id']])

print ("Tweeted: " + tweetStr)
