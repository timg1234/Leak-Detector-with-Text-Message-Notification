from twilio.rest import Client
TWILIO_ACCOUNT_SID='replace_this_text'
TWILIO_AUTH_TOKEN='replace_this_text'


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    # below is the new phone number from Twilio
    from_='(123) 456-7890',
    # below is the phone number you want the notification on
    to='(098) 765-4321',
    body='Oh hi!')

print(message.sid)
