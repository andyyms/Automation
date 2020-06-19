import os
from twilio.rest import Client

class Whatsapp:
    def auto_send(self):
        account_sid = ''
        auth_token = ''
        client = Client(account_sid)

        from_whatsapp_number = 'whatsapp:+14155238886'
        to_whatsapp_number = 'whatsapp:+852xxxxxxxx'

        self.client.messages.create(body='HI Andy Yeung',
                                    from_=from_whatsapp_number,
                                    to=to_whatsapp_number)

Whatsapp().auto_send()


