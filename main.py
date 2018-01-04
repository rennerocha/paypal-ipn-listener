import requests

from flask import Flask, request
app = Flask(__name__)

PAYPAL_PRODUCTION = 'https://ipnpb.paypal.com/cgi-bin/webscr'
PAYPAL_SANDBOX = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'

# https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNIntro/#ipn-protocol-and-architecture
# The IPN message authentication protocol consists of four steps:
#
# 1. PayPal HTTPS POSTs an IPN message to your listener that notifies it of an event.
# 2. Your listener returns an empty HTTP 200 response to PayPal.
# 3. Your listener HTTPS POSTs the complete, unaltered message back to PayPal; the message
#    must contain the same fields (in the same order) as the original message and be encoded
#    in the same way as the original message.
# 4. PayPal sends a single word back - either VERIFIED (if the message matches the original)
#    or INVALID (if the message does not match the original).


@app.route('/', methods=['POST', ])
def notification():
    ''' Listener for PayPal notification '''
    data = request.form.to_dict()

    data['cmd'] = '_notify-validate'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'www.paypal.com'}
    validation_response = requests.post(
        PAYPAL_PRODUCTION,
        data=data,
        headers=headers,
        verify=True)
    validation_response.raise_for_status()

    if validation_response == 'VERIFIED':
        # TODO do whatever you want with the notification
        pass

    return ''
