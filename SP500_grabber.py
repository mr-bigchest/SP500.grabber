from money import Money
import pandas as pd
import numpy as np
import datetime
import requests
import lxml
import html5lib
import bs4



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



''' Frame some data '''

# Make dataframe of the user's stocks and shares. Using dictionary in temporarium before GUI is developed and things are iterated further
Portfolio = pd.DataFrame.from_dict(UserStocks)
df = pd.DataFrame.from_dict(UserShares)

# Add the user shares column into the dataframe 'Portfolio'
Portfolio["Shares"] = df



''' Scrape the Web '''

url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

# due diligence required to better what the headers thing does, but I feel like I get it on a common sense level
# This is creating a function to allow python to grab data based on a url. In this case, the stock data is from Apple
def getdata(url):
  r = requests.get(url,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
  df = pd.read_html(r.text)
  return df

# run the function
df = getdata(url)

# delete the last column because it is full of text. use df.drop to remove the last n rows. df.head will do the same for the first n
df.drop(df.tail(n).index, inplace=True)


# print results
print(df)




















'''
# ID Sector info
sector_select = "stock_pick"


# match dictionary to sector selected
if sector_select == "stock_pick":
    selection = stock_pick


# ID time period
interval = 5


#input('\nGGF securities lookup for what time interval? (# of days): ')
days_back = int(interval)


# define top X highest price increases and decreases over the defined time interval
top_X = 28
stock_list = int(top_X)
X_up = stock_list - 1
X_down = stock_list * (-1)
'''