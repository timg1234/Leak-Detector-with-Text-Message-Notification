from twilio.rest import Client
import RPi.GPIO as GPIO
import time

#set up leak detection
pin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

while True:
    Status = GPIO.input(pin) 
    if Status == GPIO.HIGH:
        print("Status =", Status)
        TWILIO_ACCOUNT_SID='ADD_YOUR_SID_HERE'
        TWILIO_AUTH_TOKEN='ADD_YOUR_TOKEN_HERE'

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message1 = client.messages.create(
            from_='(123) 456-7890',
            to='(098) 765-4321',
            body='WATER HAS BEEN DETECTED IN THE PUMP ROOM!')
        print(message1.sid)

        # uncomment the five lines below if you want to notify a second person
        #message2 = client.messages.create(
        #    from_='(123) 456-7890',
        #    to='(098) 765-4321',
        #    body='WATER HAS BEEN DETECTED IN THE PUMP ROOM!')
        #print(message2.sid)
        
        time.sleep(120) # value is number of seconds between notifications
        
    else:
        print("Status =", Status)
        time.sleep(1) 

