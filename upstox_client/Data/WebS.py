from __future__ import print_function
import time
import upstox_client
from pprint import pprint
from upstox_client.Utils.Constants import *
import asyncio
import json
import ssl
import websockets
import requests
import upstox_client.Data.MarketDataFeed_pb2 as pb
from google.protobuf.json_format import MessageToDict
from datetime import datetime
import pytz
import queue
from upstox_client.LoggerConfig import logger




def get_market_data_feed_authorize_v3():
    """Get authorization for market data feed."""
    global access_token
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    url = 'https://api.upstox.com/v3/feed/market-data-feed/authorize'
    api_response = requests.get(url=url, headers=headers)
    return api_response.json()


def decode_protobuf(buffer):
    """Decode protobuf message."""
    feed_response = pb.FeedResponse()
    feed_response.ParseFromString(buffer)
    return feed_response


async def fetch_market_data():
    """Fetch market data using WebSocket and print it."""

    # Create default SSL context
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Get market data feed authorization
    response = get_market_data_feed_authorize_v3()
    # Connect to the WebSocket with SSL context
    if(response['status'] == "error"):
        print("Something went wrong while establishing connection")
        return;
    async with websockets.connect(response["data"]["authorized_redirect_uri"], ssl=ssl_context) as websocket:
        print('Connection established')

        await asyncio.sleep(1)  # Wait for 1 second

        # Data to be sent over the WebSocket
        data = {
            "guid": "someguid",
            "method": "sub",
            "data": {
                "mode": "full",
                # "instrumentKeys": ["NSE_INDEX|Nifty Bank", "NSE_INDEX|Nifty 50"]
                "instrumentKeys": ["NSE_INDEX|Nifty 50"]
            }
        }

        # Convert data to binary and send over WebSocket
        binary_data = json.dumps(data).encode('utf-8')
        await websocket.send(binary_data)

        # Continuously receive and decode data from WebSocket
        while True:
            try:
                message = await asyncio.wait_for(websocket.recv(), timeout=20)
                decoded_data = decode_protobuf(message)

                # Convert the decoded data to a dictionary
                data_dict = MessageToDict(decoded_data)

                # Print the dictionary representation
                # print(json.dumps(data_dict))
                print('Fetching...')
                if(data_dict.get('type',None) == 'live_feed'):
                    pubSub.publish(create_trade_data(data_dict.get('feeds',None).get('NSE_INDEX|Nifty 50', {}).get('ff', {}).get('indexFF', {})
                    .get('ltpc', {}).get('ltp', None),data_dict.get('currentTs',None)))
                else:
                    # pubSub.publish(-1)
                    print('Not live')
            except:
                print("No message received in 10 seconds. Waiting again...")
                #  await websocket.close() 


def convert_to_ist(ltt):
    """Convert LTT (in ms) to IST time format."""
    utc_time = datetime.utcfromtimestamp(int(ltt) / 1000)  # Convert ms to seconds
    ist_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Kolkata"))
    return ist_time.strftime("%Y-%m-%d %H:%M:%S %p")  # Format IST time

def create_trade_data(ltp, ltt):
    """Create a dictionary with LTP and converted LTT in IST."""
    return {
        "LTP": ltp,
        "LTT_IST": convert_to_ist(ltt)
    }




class PubSub:
    def __init__(self):
        print('Initialized the subscribers')
        self.subscribers = []

    def subscribe(self):
        """Each subscriber gets a queue to receive messages."""
        q = queue.Queue()
        self.subscribers.append(q)
        return q

    def publish(self, message):
        """Publish a message to all subscribers."""
        for q in self.subscribers:
            q.put(message)

pubSub = PubSub()