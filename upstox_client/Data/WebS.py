import upstox_client
from upstox_client.Utils.Constants import *

def on_message(message):
    print(message)


def main():
    print('aaaa '+access_token)
    configuration = upstox_client.Configuration()
    access_token = access_token
    configuration.access_token = access_token

    streamer = upstox_client.MarketDataStreamerV3(
        upstox_client.ApiClient(configuration), ["NSE_INDEX|Nifty 50", "NSE_INDEX|Nifty Bank"], "full")

    streamer.on("message", on_message)

    streamer.connect()


main()