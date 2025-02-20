import upstox_client
from upstox_client.Login.FileUrl import *
from upstox_client.Login.Login import *
from upstox_client.Orders.PlaceOrder import *
from upstox_client.Data.WebS import *
from upstox_client.Data.WebS import *
import asyncio
from upstox_client.Stats import *

# if __name__ == "__main__":   
#     asyncio.run(main())


# async def main():
#     await fetch_market_data()

# Call the main function inside an asyncio event loop




def start():
    # printFinalUrl()
    # getAccessToken()
    # placeOrder()
    
    processData()
    asyncio.run(fetch_market_data())
    print('called final url')


start()



