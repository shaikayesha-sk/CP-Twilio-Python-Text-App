from twilio.rest import Client  # Import using Client

# Replace these with your own Twilio account credentials
account_sid = "AC994237b93e91ce32c9a6917a5a1529a4"
auth_token = "4282f5115a35df78a81977365d8038ac"
my_cell = "+91 89195 36123"
my_twilio = "+14158959911"

client = Client(account_sid, auth_token)  # Use Client for newer versions

my_msg = 'Your message goes here...'

message = client.messages.create(to=my_cell, from_=my_twilio,
                                 body=my_msg)
