"""
This module provides all the configurations that are used for this wrapper.
Author: Omambia Dauglous
"""

class Authenticate(object):
	"""
	Configurations related to authenticting the user using the created app.
	Attributes:
		1. consumer_key: the application consumer key as provided by safaricom.
		2. consumer_secret: the application consumer secret as provided by safaricom
		3. auth_url: this is the authentication url provided
	"""
	consumer_key = "dyX8FVcKaEdoW7uATTA4wDyvPZWxIRXV"
	consumer_secret = "tKTUOfQjNup9QnUF"
	auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

class Reversal(object):
	"""
	Configuration for Reversal API.
	Attributes: 
		1.
	"""
	pass 

class LipaMpesa(object):
	"""
	Configuration for Lipa na Mpesa Online API.
	Attributes:
		1. 
	"""
	shortcode = "174379"
	pass_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"




class B2C(object):
	"""
	Configurations Specific to B2C API.
	Attributes: 
		1.
	"""
	pass 




class C2B(object):
	"""
	Configurations specific to C2B API.
	Attributes: 
		1. 
	"""
	pass

class AccountBalance(object):
	"""
	Configurations specific to AccountBalance API.
	Attributes: 
		1. initiator -> This is the credential/username used to authenticate the transaction request.
		2. security_credential ->	Base64 encoded string of the Security Credential, which is encrypted using M-Pesa public key and validates the transaction on M-Pesa Core system.
		3. command_id -> A unique command passed to the M-Pesa system.
		4. party_b -> The shortcode of the organisation receiving the transaction.
		5. receiver_identifier_type	Type of the organisation receiving the transaction.
		6. remarks	-> Comments that are sent along with the transaction.
		7. queue_time_out_URL ->	The timeout end-point that receives a timeout message.
		8. result_URL -> The end-point that receives a successful transaction.
		9. account_type	-> Organisation receiving the funds.

	"""
	initiator = "testapi"
	security_credential = "2222"
	command_id = "AccountBalance"
	party_a = "600388"
	identifier_type = "4"
	queue_time_out_url = "https://thamanionline.com/callbacks/validate"
	remarks = "Welcome to Omambia Dauglous Daraja API Wrapper"
	result_url =  "https://thamanionline.com/callbacks/validate"




class TransactionStatus(object):
	"""
	Configurations specific to Transactions status Api.
	Attributes: 
		1. 
	"""
	pass 

