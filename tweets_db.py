# Import modules
import pandas as pd
from pathlib import Path
import sqlalchemy

def make_sql_tables(engine2):
    coins_list = ["ada","bnb","btc","eth","xrp"]
    for coin in coins_list:
        create_table = f"""
        CREATE TABLE IF NOT EXISTS {coin} (
            "id" BIGINT PRIMARY KEY,
            "date" DATE,
            "time" TIME,
            "tweet" TEXT,
            "hashtags" TEXT
        )"""
        engine2.execute(create_table)

def create_coin_df(coin, dates):
    coin_df = pd.DataFrame()
    for day in dates:
        csv_path = f"./Data/{coin}/{coin}_tweets_{day}.csv"
        df = pd.read_csv(csv_path)
        coin_df = pd.concat([coin_df, df])
    return coin_df

def write_to_db(engine2):
    dates = ["2021-10-01","2021-10-02","2021-10-03","2021-10-04","2021-10-05","2021-10-06","2021-10-07","2021-10-08","2021-10-09","2021-10-10"]
    coins_list = ["ada","bnb","btc","eth","xrp"]
    make_sql_tables(engine2)
    for coin in coins_list:
        coin_df = create_coin_df(coin, dates)
        coin_df.to_sql(coin, con=engine2, if_exists='replace')


