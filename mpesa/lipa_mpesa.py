import requests 
from base64 import b64encode
from auth.auth import Authenticate
from config.credentials import LipaMpesa, AccountBalance
import  datetime
auth = Authenticate()
account = AccountBalance()

class STKPushAPI(object):
	def __init__(self):
		self.headers = { "Authorization": "Bearer %s" % auth.get_token() }
		self.url  = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
		self.timestamp = datetime.datetime.now()

	def send(self):
		print(self.timestamp)
		timestamp = str(self.timestamp).replace('-','')
		timestamp = timestamp.replace(':','')
		timestamp = timestamp.replace(' ','')
		timestamp = timestamp.replace('.','')
		print(timestamp)
		password  = b64encode(bytes(LipaMpesa().shortcode + LipaMpesa().pass_key + timestamp, 'utf-8'))
		request = {
		  "BusinessShortCode": LipaMpesa().shortcode,
		  "Password": str(password),
		  "Timestamp": str(self.timestamp),
		  "TransactionType": "CustomerPayBillOnline",
		  "Amount": "1",
		  "PartyA": "2540708067459", 
		  "PartyB": LipaMpesa().shortcode, #shortcode
		  "PhoneNumber": "2540708067459",
		  "CallBackURL": account.queue_time_out_url,
		  "AccountReference": "testpay",
		  "TransactionDesc": " Omambia Buying goods"
		}

		response = requests.post(self.url, json = request, headers = self.headers)
		return response

