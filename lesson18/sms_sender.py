# pip install twilio

from twilio.rest import Client


def send_sms(phoneNumber, message):
    account_sid = 'ACe1f3723d8ee8cf153c3152d54c1844b4'
    auth_token = '2daef877b1026a359421b29b66e9635a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='+12152537589',
        to=phoneNumber
    )
