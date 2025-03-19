
import time
import requests
from upstox_client.Data.WebS import pubSub
from upstox_client.Orders.PlaceOrder import *

def processData():
    queue = pubSub.subscribe()
    print(queue)
    while True:
        time.sleep(10)  # 5-minute interval
        print('processing data now iin nine twenty')
        # print(queue.get())
        # To be deleted
        if not queue.empty():
            data = queue.get()
            ltp = data['LTP']
            print(f'Printing ltp: {ltp}')
            placeOrder("NIFTY","PUT","SELL",ltp)
            print(f"[1m Consumer] Processed: {data}")
        else:
            print('No data in queue !!')

# Global variables
prices = []  # Stores the last 9 prices
last_ema = None  # Stores the last calculated EMA

def calculate_ema(time_period, latest_price):
    global prices, last_ema

    # Maintain rolling window of last 'time_period' prices
    prices.append(latest_price)
    if len(prices) > time_period:
        prices.pop(0)  # Remove the oldest price

    # Wait until we have enough prices to calculate EMA
    if len(prices) < time_period:
        print(f"Waiting for {time_period - len(prices)} more prices...")
        return None

    # multiplier = 2 / (time_period + 1) 
    multiplier = 0.2

    # If no previous EMA, calculate initial SMA (first EMA value)
    if last_ema is None:
        last_ema = sum(prices) / time_period
        print(f"Initial EMA (SMA): {last_ema}")
        return last_ema

    # Calculate EMA using the last EMA
    last_ema = (latest_price - last_ema) * multiplier + last_ema
    print(f"Updated 9EMA: {last_ema}")
    
    return last_ema

# Simulating price updates
# price_data = [22853, 22872, 22894, 22921, 22915, 22917, 22947, 22948, 22941, 22950]

# for price in price_data:
#     calculate_ema(9, price)

    