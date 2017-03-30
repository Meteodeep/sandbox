# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+12316851234", from_="+15555555555",
                                     body="Hello there!")
                                     
#MMS

message = client.messages.create(to="+12316851234", from_="+15555555555",
                                     body="Hello there!",
                                     media_url=['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])
