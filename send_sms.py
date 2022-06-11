# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from file_reader import read_token

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

account_sid = read_token('TWILIO_ACCOUNT_SID')
auth_token = read_token('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token, queue_num)
message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=read_token('FROM_PHONE'),
                     to=read_token('TO_PHONE')
                 )

print(message.sid)
