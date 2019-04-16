import requests
from config.credentials import AccountBalance
from auth.auth import Authenticate
account = AccountBalance()
class AccountBalanceAPI(object):
    def __init__(self):
        self.headers  = { "Authorization": "Bearer %s" % Authenticate().get_token() }
        self.url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"

    def send(self):
        request = { "Initiator": account.initiator,
                    "SecurityCredential": str(Authenticate().get_encrypted_password()),
                    "CommandID":"AccountBalance",
                    "PartyA": account.party_a,
                    "IdentifierType":account.identifier_type,
                    "Remarks":account.remarks,
                    "QueueTimeOutURL":account.queue_time_out_url,
                    "ResultURL":account.result_url
        }
        response = requests.post(self.url, json = request, headers=self.headers)

        return response.text