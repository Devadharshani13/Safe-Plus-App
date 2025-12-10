"""
Send messaage and make call.
"""
from tuna.settings import (AUTH_TOKEN,
                           ACCOUNT_SID,
                           TWILIO_PHONE_NUMBER)
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


def make_call(to_number, message):
    """Make an automated voice call with a message."""
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        call = client.calls.create(
            to=to_number,
            from_=TWILIO_PHONE_NUMBER,
            twiml=f"<Response><Say>{message}</Say></Response>"
        )
        
        print(f"Call placed successfully! Call SID: {call.sid}")
        return {"success": True, "call_sid": call.sid}
    
    except TwilioRestException as e:
        print(f"Error making call: {e}")
        return {"success": False, "error": str(e)}


def send_sms(to_number, message):
    """Send an SMS using Twilio API."""
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        sms = client.messages.create(
            to=to_number,
            from_=TWILIO_PHONE_NUMBER,
            body=message
        )

        print(f"Message sent successfully! Message SID: {sms.sid}")
        return {"success": True, "message_sid": sms.sid}

    except TwilioRestException as e:
        print(f"Error sending SMS: {e}")
        return {"success": False, "error": str(e)}
