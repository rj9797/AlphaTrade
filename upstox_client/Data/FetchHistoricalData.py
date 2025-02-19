import pandas as pd

scripts = pd.read_csv('https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz');

def getInstrumentKey(symbol):
    print(scripts[scripts['tradingsymbol'] == symbol]['instrument_key'])
    return scripts[scripts['tradingsymbol'] == symbol]['instrument_key']