import os
from twilio.rest import Client

sid = os.environ["TWILIO_ACCOUNT_SID"]
token = os.environ["TWILIO_AUTH_TOKEN"]
from_number = os.environ["TWILIO_FROM"]
to_number = os.environ.get("ORDER_TO", "+15592176778")  # Johnny Williams
body = (os.environ.get("ORDER_MESSAGE") or "").strip()

if not body:
    raise SystemExit("No order message received; nothing to send.")

msg = Client(sid, token).messages.create(body=body, from_=from_number, to=to_number)
print(f"Sent to {to_number}. SID: {msg.sid}")
