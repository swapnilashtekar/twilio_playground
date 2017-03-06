#!/usr/bin/env python

import datetime
import os
import random
from twilio.rest import TwilioRestClient
import subprocess
import sys
from time import strftime



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


# Phone numbers
my_number = os.environ.get('MY_NUMBER')
her_number = os.environ.get('HER_NUMBER')

reasons = [
  'Working hard',
  'Gotta ship this feature',
  'Someone fucked the system again'
]

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    to = my_number,
    from_= her_number,
    body = "Late at work. " + random.choice(reasons),
)

print message.sid

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