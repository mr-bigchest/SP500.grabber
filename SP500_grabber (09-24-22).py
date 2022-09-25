''' Imports '''

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


''' Dictionaries '''

UserStocks = {"Stocks": ['SIL', 'UUP', 'XLRE', 'PRPFX', 'AAPL', 'CSCO', 'ORCL', 'VZ', 'PSCF', 'XLF', 'AGO', 'BX', 'BAX', 'GILD', 'UNH', 'XLV', 'DG', 'F', 'WHR', 'XLP', 'XLY', 'UPS', 'LMT', 'MPC', 'REGI', 'VLO', 'XLE', 'ISTB']}
UserShares = {"Shares": [140, 697, 146, 462.907, 140, 70, 220, 114, 197, 300, 140, 135, 207, 125, 55, 266, 150, 400, 9, 275, 165, 75, 76, 149, 389, 148, 181, 520]}
SectorTracker = {"S&P500 Indexes": ['XLRE', 'XLE', 'XLF', 'XLK', 'XLV', 'XLY', 'XLI', 'XLP', 'XLB', 'XLU', 'XLC']}
Alternatives = {"Alternatives": ['SIL', 'UUP', 'XLRE', 'PRPFX']}
Technology = {"Technology": ['AAPL', 'CSCO', 'ORCL', 'VZ']}
Financials = {"Financials": ['PSCF', 'XLF', 'AGO', 'BX']}
HealthCare = {"Health Care": ['BAX', 'GILD', 'UNH', 'XLV']}
ConsumerGoods = {"Consumer Goods": ['DG','F', 'WHR', 'XLP', 'XLY']}
Industrials = {"Industrials": ['LMT']}
Materials = {"Materials": ['UPS']}
Energy = {"Energy": ['MPC', 'REGI', 'VLO', 'XLE']}
FixedIncome = {"Fixed Income": ['ISTB']}
Communications = {"Communications": ['XLC']}
Ticker_Names = {
    'SIL': 'GLB X FUNDS/GLB X SILVER MINERS', 'UUP': 'INVESCO DB DLR /BULLISH FD', 'XLRE': 'SELECT SECTOR S/RL EST SELECT SECT',
    'PRPFX': 'Permanent Portfolio Permanent Portfolio Class I', 'AAPL': 'Apple Inc.', 'CSCO': 'Cisco Systems, Inc.', 'ORCL': 'Oracle Corporation',
    'VZ': 'Verizon Communications Inc.', 'PSCF': 'INVESCO S&P SMALLCAP FINANCIALS ETF', 'XLF': 'Financial Select Sector SPDR Fund',
    'AGO': 'Assured Guaranty Ltd.', 'BX': 'Blackstone Group Inc', 'BAX': 'Baxter International Inc', 'GILD': 'Gilead Sciences, Inc.',
    'UNH': 'UnitedHealth Group Inc', 'XLV': 'SELECT SECTOR S/HEALTH CARE', 'DG': 'Dollar General Corp.', 'F': 'Ford Motor Company',
    'WHR': 'Whirlpool Corporation', 'XLP': 'Consumer Staples Select Sector SPDR Fund', 'XLY': 'Consumer Discretionary Select Sector SPDR Fund',
    'UPS': 'United Parcel Service, Inc.', 'LMT': 'Lockheed Martin Corporation', 'MPC': 'Marathon Petroleum Corp', 'REGI': 'Renewable Energy Group Inc',
    'VLO': 'Valero Energy Corporation', 'XLE': 'SELECT SECTOR S/ENERGY', 'ISTB': 'ISHARES TR/CORE 1-5 YR USD BD',}


''' Frame user portfolio data '''

Portfolio = pd.DataFrame.from_dict(UserStocks) # Make dataframe of the user's stocks and shares (in temporarium before GUI)
df = pd.DataFrame.from_dict(UserShares)
Portfolio["Shares"] = df # Add the user shares column into the dataframe 'Portfolio'



''' Scrape web to collect historical portfolio data '''

def StockHistory(symbol): # get the historical data for a stock
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'close',
    'DNT': '1', # Do Not Track Request Header
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537. 36 OPR/90.0.4480.84'} # my user agent. have to make it for the user to probably put in on GUI or something
  url = f'http://finance.yahoo.com/quote/{symbol}/history?p={symbol}'
  r = requests.get(url, headers=headers)

  dfs = pd.read_html(r.content) # gets list of dataframes
  df = dfs[0] # picks out the dataframe we want
  df.drop(df.tail(1).index, inplace=True) # cuts text qualifier at the bottom
  df = df[df['Open'].str.contains('Dividend') == False] # removes dividend rows

  df['Date'] = pd.to_datetime(df['Date']) # converts to datetime
  numericals = list(df.columns)[1::] # makes a list of non-date columns for replacement

  for colname in numericals:
    df[colname] = df[colname].str.replace(',','') # just in case, get rid of commas
    df[colname] = df[colname].astype(np.float64) # convert to float

  return df


# NOTE: when you are getting the content back via pd.read_html, pandas is returning to you a LIST OF DATFRAMES, not just a dataframe. So you need to just get the first dataframe out of there before oyu start wonking with everything.


df = StockHistory('AAPL')




print(df)
print(df.dtypes)




# alright the code does a basic purpose again. time to make a GUI



''' REVAMPING - SpotCheck     also I don't need it right now.
# print(r.status_code) to check for 404; print(soup.title.text) to check title of site to make sure it works
def SpotCheck(symbol): # do a spot check on current price, $ delta & % delta a/o previous close
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'close',
    'DNT': '1', # Do Not Track Request Header
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537. 36 OPR/90.0.4480.84'} # my user agent. have to make it for the user to probably put in on GUI or something
  url = f'https://finance.yahoo.com/quote/{symbol}'
  r = requests.get(url, headers=headers)
  soup = BeautifulSoup(r.text, 'html.parser')

  stock = {
    'symbol': symbol,
    'price': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'delta': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    'percent delta': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
  }
  return stock

mystocks = ['SPY', 'LMT', 'AAPL']
stockdata = []

#for i in mystocks: stockdata.append(SpotCheck(i))

#print(stockdata)

# alright cool. so this works. now I need it to do this for a portfolio and also get the historical data. i also need to revamp the outputting process. i currently dislike the way it works


- make it output to dataframe
- make the data non-text
'''