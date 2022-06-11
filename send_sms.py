# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from file_reader import read_token

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

class smsObject():
    def __init__(self):
        self.account_sid = None
        self.auth_token = None
        self.queue_num = None
        self.from_phone = None
        self.to_phone = None
        self.client = None
    
    def createClient(self):
        self.account_sid = read_token('TWILIO_ACCOUNT_SID')
        self.auth_token = read_token('TWILIO_AUTH_TOKEN')
        self.from_phone = read_token('FROM_PHONE')
        self.to_phone = read_token('TO_PHONE')
        self.client = Client(self.account_sid, self.auth_token)


    def setQueueNum(self, val):
        self.queue_num = val

    def sendMsg(self):
        message = self.client.messages \
                        .create(
                            body=f"Get ready to play! You are {self.queue_num} in line.",
                            from_=self.from_phone,
                            to=self.to_phone
                        )
        print(message.sid)


if __name__ == '__main__':
    notifier = smsObject()
    notifier.createClient()
    notifier.setQueueNum(200)
    notifier.sendMsg()


