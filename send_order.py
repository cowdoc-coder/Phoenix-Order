import os
from twilio.rest import Client

sid = os.environ["TWILIO_ACCOUNT_SID"]
token = os.environ["TWILIO_AUTH_TOKEN"]
from_number = os.environ["TWILIO_FROM"]
recipients = os.environ.get("ORDER_TO", "+15592176778")
body = (os.environ.get("ORDER_MESSAGE") or "").strip()

if not body:
    raise SystemExit("No order message received; nothing to send.")

client = Client(sid, token)
numbers = [n.strip() for n in recipients.split(",") if n.strip()]
for to_number in numbers:
    msg = client.messages.create(body=body, from_=from_number, to=to_number)
    print(f"Sent to {to_number}. SID: {msg.sid}")
