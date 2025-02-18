import requests
from upstox_client.Utils.Constants import *

def placeOrder():
    print('Access_TOkkkkk: '+access_token)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}',
    }
    data = {
        'quantity': 75,
        'product': 'D',
        'validity': 'DAY',
        'price': 0.0,
        'tag': 'string',
        'instrument_token' : 'NSE_FO|63491',
        'order_type' : 'MARKET',
        'transaction_type': 'BUY',
        'trigger_price': 13.2,
        'is_amo': False,
    }

    try:
        response = requests.post(place_order_url, json=data, headers=headers)
        print('Response Code:', response.status_code)
        print('Response Body for placed order:', response.json())

    except Exception as e:
        print('Error while placing order:', str(e))