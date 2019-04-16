"""
This modules authenticate the user to the Daraja APIs
"""
import requests
import os
import json
from requests.auth import HTTPBasicAuth
from M2Crypto import RSA, X509
from base64 import b64encode

from config.credentials import Authenticate, AccountBalance

# object creations
auth = Authenticate()
account = AccountBalance()
base_dir = os.path.dirname(os.path.realpath(__file__))

class Authenticate(object):
	"""
	Authenticate the user:
	Methods:
		get_token() -> 
			Return  authentication token for the user
		get_encrypted_password() -> 
			Returns the encrypted password using the safaricom algorithm
	"""

	def get_token(self):
		results = requests.get(auth.auth_url, 
				auth = HTTPBasicAuth(auth.consumer_key, auth.consumer_secret) )
		data  = json.loads(results.text)

		return data['access_token']

	def get_encrypted_password(self):
		with open(os.path.join(base_dir, 'cert.cer'), mode = 'r') as f:
			cert = X509.load_cert_string(f.read()) #reading the file content 
			#pub_key = X509.load_cert_string(f.read())
			pub_key = cert.get_pubkey()
			rsa_key = pub_key.get_rsa()
			cipher = rsa_key.public_encrypt(bytes(account.security_credential,'utf-8'), RSA.pkcs1_padding)
			return  b64encode(cipher)