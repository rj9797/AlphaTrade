import pandas as pd
from datetime import datetime, time
from upstox_client.Utils.Constants import *
import requests
from upstox_client.LoggerConfig import logger
from upstox_client.Utils.Utility import *


def getInstrumentKey(symbol):
    print(scripts[scripts['tradingsymbol'] == symbol]['instrument_key'])
    return scripts[scripts['tradingsymbol'] == symbol]['instrument_key']

def getData(symbol, interval, date_from, date_to):
    inst_Token = getInstrumentKey(symbol)
    logger.info("FetchHistoricalDataInstrument token {inst_Token}")
    url = f'https://api.upstox.com/v2/historical-candle/{inst_Token.values[0]}/{interval}/{date_to}/{date_from}'
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    # Check the response status
    if response.status_code == 200:
        formatted_data = decodeHistoricalData(response.json())
        return formatted_data
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")
    # data = pd.DataFrame.from_dict(response.json()['data']['candles'])
# print(getData('NIFTY27FEB22850PE','30minute','2025-02-05','2025-02-10'))


def decodeHistoricalData(response):
    formatted_data = [
        {
            'timestamp': convert_date(candle[0]),
            'open': candle[1],
            'high': candle[2],
            'low': candle[3],
            'close': candle[4],
            'volume': candle[5],
            'open_interest': candle[6]
        }
        for candle in response['data']['candles']
    ]

    return formatted_data