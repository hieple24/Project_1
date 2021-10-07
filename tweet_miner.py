import twint
from datetime import date
tickers = ["#ada","#btc","#xrp","#bnb","#eth","cardano","bitcoin","xrp","bnb","ethereum"]
today = date.today()

def crypto_scraper(ticker_list):
    for ticker in ticker_list:   
        # Configure
        c = twint.Config()
        c.Search = ticker
        c.Store_json = True
        c.Output = f"./data/{ticker}_data_{today}.json"
        #c.Until = '2021-10-05'
        twint.run.Search(c)

def coin_miner(coin):
        c = twint.Config()
        c.Search = coin
        c.Store_json = True
        c.Output = f"./data/{coin}_data_{today}.json"
        # Run
        twint.run.Search(c)

coin_miner("bitcoin")