import upstox_client
from upstox_client.Login.FileUrl import *
from upstox_client.Login.Login import *
from upstox_client.Orders.PlaceOrder import *
from upstox_client.Data.WebS import *
import asyncio

# if __name__ == "__main__":
#     asyncio.run(main())


# async def main():
#     await fetch_market_data()

# Call the main function inside an asyncio event loop


def getFileUrl():
    # printFinalUrl()
    # getAccessToken()
    # placeOrder()
    asyncio.run(fetch_market_data())
    print('called final url')


getFileUrl()



