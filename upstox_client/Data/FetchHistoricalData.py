import pandas as pd
from datetime import datetime, time
from upstox_client.Utils.Constants import *
import requests


def getInstrumentKey(symbol):
    print(scripts[scripts['tradingsymbol'] == symbol]['instrument_key'])
    return scripts[scripts['tradingsymbol'] == symbol]['instrument_key']

def getData(symbol, interval, date_from, date_to):
    inst_Token = getInstrumentKey(symbol)
    print("Intruemmmmm "+inst_Token)
    url = f'https://api.upstox.com/v2/historical-candle/{inst_Token.values[0]}/{interval}/{date_to}/{date_from}'
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    # Check the response status
    if response.status_code == 200:
        print(response.json())
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")
    # data = pd.DataFrame.from_dict(response.json()['data']['candles'])


# print(getData('NIFTY27FEB22850PE','30minute','2025-02-05','2025-02-10'))