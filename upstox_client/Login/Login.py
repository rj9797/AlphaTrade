import requests
from upstox_client.Utils.Constants import *;

class Login:
    def getAccessToken(self):
        print('hiopi')
        url = 'https://api.upstox.com/v2/login/authorization/token'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'code': code,
            'client_id': client_id,
            'client_secret': secret_key,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code',
        }
        response = requests.post(url, headers=headers, data=data)

        print(response.status_code)
        print(response.json())
        new_access_token = response.json()['access_token']
        access_token = new_access_token

    
    # def writeToFile(data, file_path):
    #     try:
    #         with open(file_path, 'w') as file:
    #             file.write(data)
    #         print(f"Data written to {file_path}")
    #     except Exception as e:
    #         print(f"Error writing to file: {e}") 
loginObj = Login()
# loginObj.getAccessToken()