import pandas as pd

# Auth
api_key = 'bb02757d-42fd-4ed1-b4bb-e0c64dbb2825'
client_id = '41ba6a51-565b-42a3-8daf-d7257b2714df'
secret_key = 'm4qauwxr5v'
redirect_uri = 'https://pro.upstox.com/holdings'
finalUrl = f'https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}'
code = 'EvU0FQ'
access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIxNjg5MTIiLCJqdGkiOiI2N2Y4ZTdmMWE4NTIyZDRhOWM4MWZhYmYiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzQ0MzY1NTUzLCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDQ0MDg4MDB9.vnbGwLLT2m6yPkM0qjoVH5iWYt18yyhDeCotZY_3xmo'

# Orders
place_order_url = 'https://api-hft.upstox.com/v2/order/place'

# Scripts
scripts = pd.read_csv('https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz');
