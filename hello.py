import upstox_client
from upstox_client.Login.FileUrl import *
from upstox_client.Login.Login import *
from upstox_client.Orders.PlaceOrder import *
from upstox_client.Data.WebS import fetch_market_data

def getFileUrl():
    # printFinalUrl()
    # getAccessToken()
    # placeOrder()
    fetch_market_data()
    print('called final url')

getFileUrl()



