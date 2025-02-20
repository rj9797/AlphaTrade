import upstox_client
from upstox_client.Login.FileUrl import *
from upstox_client.Login.Login import *
from upstox_client.Orders.PlaceOrder import *
from upstox_client.Data.WebS import *
from upstox_client.Data.WebS import *
import asyncio
from upstox_client.Stats.NineTwenty import *
import threading

# if __name__ == "__main__":   
#     asyncio.run(main())


# async def main():
#     await fetch_market_data()

# Call the main function inside an asyncio event loop




def run_async_fetch_market_data(event):
    """Run fetch_market_data and signal when ready."""
    print(event)
    event.set()
    asyncio.run(fetch_market_data())  # Pass the event to fetch_market_data

def start():
    # Create an event to signal when fetch_market_data is ready
    ready_event = threading.Event()

    # Start fetch_market_data thread
    process_thread2 = threading.Thread(target=run_async_fetch_market_data, args=(ready_event,), daemon=True)
    process_thread2.start()
    print('waiting')
    # Wait for fetch_market_data to signal readiness
    ready_event.wait()  # Blocks until fetch_market_data sets the event
    print('waiting complete')
    # Start processData thread
    process_thread1 = threading.Thread(target=processData, daemon=True)
    process_thread1.start()

    print('called final url')

    process_thread2.join()
    process_thread1.join()


if __name__ == "__main__":
    start()



