import requests
from upstox_client.Utils.Constants import *
from upstox_client.Utils.MapData import *
import math

def placeOrder(index,option_type, transaction_type, spot_price):
    if index not in NSE_MAP:
        # SEND SMS
        print(f"The given index key {index} does not exist in map, it does not have instrument key")
        return -1


    instrumentKey = NSE_MAP[index]
    strike_price = None
    if(index == "NIFTY"):
        if(option_type == "CALL"):
            strike_price = nearest_strike_price_call(spot_price, 50)
    else:
        # SEND SMS
        print(f"The given index key {index} is unknow in the code conditions")
        return -1



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

def getInstrumentToken(instrumentKey, expiryDate):
    url = 'https://api.upstox.com/v2/option/chain'
    params = {
        'instrument_key': 'NSE_INDEX|Nifty 50',
        'expiry_date': '2025-03-06'
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, params=params, headers=headers)
    # opt_chain_table = pd.DataFrame.from_dict(response.json()['data'])
    option_chain = response.json()['data']


def nearest_strike_price_call(spot_price, strike_increment):
    # Round down to the nearest multiple of the strike increment
    nearest_strike = math.floor(spot_price / strike_increment) * strike_increment
    return nearest_strike

def nearest_strike_price_put(spot_price, strike_increment):
    # Round down to the nearest multiple of the strike increment
    nearest_strike = math.floor(spot_price / strike_increment) * strike_increment
    return nearest_strike