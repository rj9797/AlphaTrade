import upstox_client
from upstox_client.Login.FileUrl import *
from upstox_client.Login.Login import *
from upstox_client.Orders.PlaceOrder import *
from upstox_client.Data.WebS import *
from upstox_client.Data.WebS import *
import asyncio
from upstox_client.Stats.NineTwenty import *
import threading


async def main():
    """Start WebSocket fetcher in the main thread."""
    await fetch_market_data()

# Call the main function inside an asyncio event loop


def start():
    """Start WebSocket (async) & Consumer (threading) properly."""
    # placeOrder()
    # Start price consumer in a separate thread
    process_thread = threading.Thread(target=processData, daemon=True)
    process_thread.start()

    print("Starting")
    # Run WebSocket fetcher in the main asyncio event loop
    asyncio.run(main())  # Runs fetch_market_data()
    process_thread.join()
    

if __name__ == "__main__":
    start()



