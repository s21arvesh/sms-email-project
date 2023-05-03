import CLASS
from twilio.rest import Client

""" client initialises the account_sid and auth key """
client = Client(CLASS.account_sid, CLASS.auth_token)

message = client.messages.create(
    body="THIS IS FOR TRIAL PURPOSE",
    from_=CLASS.twilio_number,
    to=CLASS.my_phone_number
)
