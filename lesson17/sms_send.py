
from twilio.rest import Client
account_sid = 'AC0746ee39e21a67a3d542917320ce05ab'
auth_token = 'a7b8a717325aa94966fbba3b30e3800b'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='asdsd!',
    from_='+14156891572',
    to='+77055759541'
)

print(message.sid)
