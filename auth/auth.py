"""
This modules authenticate the user to the Daraja APIs
"""
import requests
import os
import json
from requests.auth import HTTPBasicAuth
from M2Crypto import RSA, X509
from base64 import b64encode

from config.credentials import Authenticate

# object creations
auth = Authenticate()

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
		results = requests.get(auth.api_url, 
				auth = HTTPBasicAuth(auth.consumer_key, consumer_secret) )
		data  = json.loads(results)

		return data['access_token']

	def get_encrypted_password(self):
		
