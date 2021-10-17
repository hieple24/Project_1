# Crypto Prices vs. Twitter Mentions

## Project Goals
Explore the relationship between the price of cryptocurrencies and their mentions and counts  on Twitter
 
Is there a  linear relationship between Twitter mentions and cryptocurrency price? 
What direction does the price move in?

Cryptocurrencies analyzed  (Top 5 market cap):
- BTC
- ETH
- ADA
- BNB
- XRP


## Collecting Crypto Tweets

To collect twiiter feed the twint libary was used. By using the cyrpto_scraper function you can colect tweets containing the string values in the tickers list. Alternatively, you can use the coin_miner function and pass in a string value of the text in tweets you want to collect.
![Screenshot of code to collect tweets](./images/tweet_miner.png)

## Wordcloud Visualizations

To help visualize text that is frequently used in tweets the wordcloud library was used. By comparing the wordclouds of the crypto currencies we can see that they all have other cyrtpo currency mentions, especially "btc" and "bitcoin".

![Image of ADA wordcloud](./images/ada_wordcloud.png)
![Image of BNB wordcloud](./images/bnb_wordcloud.png)
![Image of BTC wordcloud](./images/btc_wordcloud.png)
![Image of ETH wordcloud](./images/eth_wordcloud.png)
![Image of XRP wordcloud](./images/xrp_wordcloud.png)