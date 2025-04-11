import requests
from upstox_client.Utils.Constants import *
from datetime import datetime, time

def getInstrumentTokenForOptions(instrumentKey, expiryDate, option_type,strike_price):
    url = 'https://api.upstox.com/v2/option/chain'
    params = {
        'instrument_key': 'NSE_INDEX|Nifty 50',
        'expiry_date': '2025-04-17'
        # 'instrument_key': instrumentKey,
        # 'expiry_date': expiryDate
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, params=params, headers=headers)
    # opt_chain_table = pd.DataFrame.from_dict(response.json()['data'])
    # option_chain = response.json()['data']
    option_chain = response.json()
    print(f'Response::: {option_chain.get('status')}')
    if option_chain is not None and option_chain.get('status') == 'success':
         for entry in option_chain["data"]:
            if entry["strike_price"] == strike_price:
                if option_type.lower() == "call":
                    print(entry["call_options"]["market_data"]["ltp"])
                    return entry["call_options"]["instrument_key"]
                elif option_type.lower() == "put":
                    print(entry["call_options"]["market_data"]["ltp"])
                    return entry["put_options"]["instrument_key"]
    else:
        print('Failed to fetch instrument token')

def convert_date(row):
    return datetime.fromisoformat(row).strftime('%Y-%m-%d %H:%M:%S')

def liveEmaCalculation(interval,prevEma):
    k = 2 / (period + 1)
    currEma = (price - prev_ema) * k + prev_ema
    return currEma