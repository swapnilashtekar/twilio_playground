#!/usr/bin/env python

import datetime
import os
import random
from twilio.rest import TwilioRestClient
import subprocess
import sys
from time import strftime


def sentMessages(client):
    for message in client.messages.list():
        print message.body

today = datetime.date.today()

# skip weekends
#if today.strftime('%A') == 'Saturday' or today('%A') == 'Sunday':
#    sys.exit()

# exit if no sessions with my username are found
#output = subprocess.check_output('who')
#if 'my_username' not in output:
#    sys.exit()


# returns 'None' if the key doesn't exist
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN  = os.environ.get('TWILIO_AUTH_TOKEN')
print TWILIO_ACCOUNT_SID

# Phone numbers
HER_NUMBER = os.environ.get('HER_NUMBER')
MY_NUMBER = os.environ.get('MY_NUMBER')
print HER_NUMBER
print MY_NUMBER

reasons = [
    'Working hard',
    'Gotta ship this feature',
    'Someone fucked the system again',
    'Picking some stuff from grocery store',
    'Cricket practice',
    'Traffic sucks'
]

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

"""
If you are sedning message from short code service of Twilio, use from_
"""

message = client.messages.create(
    to = '{}'.format(HER_NUMBER),
    from_= '{}'.format(MY_NUMBER),
    body = "Late at work. " + random.choice(reasons),
    media_url="http://images.huffingtonpost.com/2015-08-21-1440138242-5865807-bazingasheldon.jpg"
)

print "This message is sent : ",message.sid

print sentMessages(client)

try:
    f = open('logs/file.txt', 'a')
except IOError as e:
    # dir & file don't exist; create them
    os.mkdir('logs')
    f = open('logs/file.txt', 'a')
except Exception as e:
    print e
else:
    pass

# log it
f.write("Message sent at " + strftime("%a, %d %b %Y %H:%M:%S") + "\n")
f.close()