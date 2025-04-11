
import time as t
import datetime
import requests
from upstox_client.Data.WebS import pubSub
from upstox_client.Orders.PlaceOrder import *
from datetime import datetime,timedelta
from pytz import timezone 
from upstox_client.Data.FetchHistoricalData import getData

def processLiveData():
    queue = pubSub.subscribe()
    print(queue)
    while True:
        print('Reached process data')
        wait_until_next_minute() # 1-minute interval
        current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        print(f'processing data now iin nine twenty time: {current_time}')
        current_price = queue.get()
        print(f'Fetched the price for 1 minute {current_price}')
        calculate_ema(9,current_price)
        # To be deleted
        if not queue.empty():
            data = queue.get()
            ltp = data['LTP']
            print(f'Printing ltp: {ltp}')
            # placeOrder("NIFTY","PUT","SELL",ltp)
            print(f"[1m Consumer] Processed: {data}")
        else:
            print('No data in queue !!')

# Global variables
prices = []  # Stores the last 9 prices
last_ema = None  # Stores the last calculated EMA

def calculate_ema(time_period, latest_price):
    logger.info(f'Calculating EMA now {time_period} {latest_price}')
    global prices, last_ema

    # Maintain rolling window of last 'time_period' prices
    prices.append(latest_price)
    if len(prices) > time_period:
        prices.pop(0)  # Remove the oldest price

    # Wait until we have enough prices to calculate EMA
    if len(prices) < time_period:
        print(f"Waiting for {time_period - len(prices)} more prices...")
        return None

    multiplier = 2 / (time_period + 1) 
    # multiplier = 0.2

    # If no previous EMA, calculate initial SMA (first EMA value)
    if last_ema is None:
        last_ema = sum(prices) / time_period
        print(f"Initial EMA (SMA): {last_ema}")
        return last_ema

    # Calculate EMA using the last EMA
    last_ema = (latest_price - last_ema) * multiplier + last_ema
    print(f"Updated 9EMA: {last_ema}")
    
    return last_ema


def wait_until_next_minute():
    now = datetime.now()
    next_minute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
    wait_seconds = (next_minute - now).total_seconds()
    t.sleep(wait_seconds)


def testEfficiency():
    formatted_data = getData('NIFTY','30minute','2025-02-05','2025-02-10')
    closing_price = [candle['close'] for candle in reversed(formatted_data)]
    logger.info(f'Test efficiency -> {formatted_data}')


    