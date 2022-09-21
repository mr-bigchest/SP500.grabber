from pandas_datareader import data as pdr
from money import Money
import yfinance as yf
import pandas as pd
import datetime
import sys
import re
import os

# Dictionaries
ggf = {
    'SIL': 'ggf', 'UUP': 'ggf', 'XLRE': 'ggf', 'PRPFX': 'ggf', 'AAPL': 'ggf', 'CSCO': 'ggf', 'ORCL': 'ggf', 'VZ': 'ggf', 'PSCF': 'ggf',
    'XLF': 'ggf', 'AGO': 'ggf', 'BX': 'ggf', 'BAX': 'ggf', 'GILD': 'ggf', 'UNH': 'ggf', 'XLV': 'ggf', 'DG': 'ggf', 'F': 'ggf', 'WHR': 'ggf',
    'XLP': 'ggf', 'XLY': 'ggf', 'UPS': 'ggf', 'LMT': 'ggf', 'MPC': 'ggf', 'REGI': 'ggf', 'VLO': 'ggf', 'XLE': 'ggf', 'ISTB': 'ggf',}

sp = {
    'XLRE': 'sp', 'XLE': 'sp', 'XLF': 'sp', 'XLK': 'sp', 'XLV': 'sp', 'XLY': 'sp', 'XLI': 'sp', 'XLP': 'sp', 'XLB': 'sp', 'XLU': 'sp'}

shares = {
    'SIL': '140', 'UUP': '697', 'XLRE': '146', 'PRPFX': '462.907', 'AAPL': '140', 'CSCO': '70', 'ORCL': '220', 'VZ': '114', 'PSCF': '197',
    'XLF': '300', 'AGO': '140', 'BX': '135', 'BAX': '207', 'GILD': '125', 'UNH': '55', 'XLV': '266', 'DG': '150', 'F': '400', 'WHR': '9',
    'XLP': '275', 'XLY': '165', 'UPS': '75', 'LMT': '76', 'MPC': '149', 'REGI': '389', 'VLO': '148', 'XLE': '181', 'ISTB': '520',}

sector_of_share = {
    'SIL': 'Alternatives', 'UUP': 'Alternatives', 'XLRE': 'Alternatives', 'PRPFX': 'Alternatives', 'AAPL': 'IT & Telecom', 'CSCO': 'IT & Telecom',
    'ORCL': 'IT & Telecom', 'VZ': 'IT & Telecom', 'PSCF': 'Financials', 'XLF': 'Financials', 'AGO': 'Financials', 'BX': 'Financials',
    'BAX': 'Health Care', 'GILD': 'Health Care', 'UNH': 'Health Care', 'XLV': 'Health Care', 'DG': 'Consumer Goods', 'F': 'Consumer Goods',
    'WHR': 'Consumer Goods', 'XLP': 'Consumer Goods', 'XLY': 'Consumer Goods', 'UPS': 'Industrials & Materials', 'LMT': 'Industrials & Materials',
    'MPC': 'Energy', 'REGI': 'Energy', 'VLO': 'Energy', 'XLE': 'Energy', 'ISTB': 'Fixed Income',}

ticker_full_name = {
    'SIL': 'GLB X FUNDS/GLB X SILVER MINERS', 'UUP': 'INVESCO DB DLR /BULLISH FD', 'XLRE': 'SELECT SECTOR S/RL EST SELECT SECT',
    'PRPFX': 'Permanent Portfolio Permanent Portfolio Class I', 'AAPL': 'Apple Inc.', 'CSCO': 'Cisco Systems, Inc.', 'ORCL': 'Oracle Corporation',
    'VZ': 'Verizon Communications Inc.', 'PSCF': 'INVESCO S&P SMALLCAP FINANCIALS ETF', 'XLF': 'Financial Select Sector SPDR Fund',
    'AGO': 'Assured Guaranty Ltd.', 'BX': 'Blackstone Group Inc', 'BAX': 'Baxter International Inc', 'GILD': 'Gilead Sciences, Inc.',
    'UNH': 'UnitedHealth Group Inc', 'XLV': 'SELECT SECTOR S/HEALTH CARE', 'DG': 'Dollar General Corp.', 'F': 'Ford Motor Company',
    'WHR': 'Whirlpool Corporation', 'XLP': 'Consumer Staples Select Sector SPDR Fund', 'XLY': 'Consumer Discretionary Select Sector SPDR Fund',
    'UPS': 'United Parcel Service, Inc.', 'LMT': 'Lockheed Martin Corporation', 'MPC': 'Marathon Petroleum Corp', 'REGI': 'Renewable Energy Group Inc',
    'VLO': 'Valero Energy Corporation', 'XLE': 'SELECT SECTOR S/ENERGY', 'ISTB': 'ISHARES TR/CORE 1-5 YR USD BD',}

# ID Sector info
sector_select = "ggf"

# match dictionary to sector selected
if sector_select == "ggf":
    selection = sp

# ID time period
interval = 56
#input('\nGGF securities lookup for what time interval? (# of days): ')
thyme = int(interval)
# ID gainers and losers
gain_or_lose = 28
#input('\nNumber of gainers? [full list = 28] ')
gl = int(gain_or_lose)
tops = gl - 1
bots = gl * (-1)

# split dict into two lists
keys, values = zip(*selection.items())
print ("keys : ", str(keys))
print()
print()

# add share vals
runes, codex = zip(*shares.items())
print ("codex : ", str(codex))
print()
print()


# add names to be later associated
key3, hole3 = zip(*ticker_full_name.items())
print ("hole3 : ", str(hole3))
print()
print()

key4, hole4 = zip(*sector_of_share.items())
print("hole4: ", str(hole4))
print()
print()

# get dates based on selected time interval
t_fin = datetime.date.today()
t_ini = t_fin - datetime.timedelta(days=thyme)

# this made the downloader work ¯\_(ツ)_/¯
yf.pdr_override()

# downloads selected sector list
downloading = True
j = 0

while downloading == True:
    raw_info = pdr.get_data_yahoo(keys[j], start=t_ini, end=t_fin)
    saveit = raw_info.to_excel(str(keys[j] + '.xlsx'))

    j = j + 1
    if j == len(values):
        downloading = False

# deletes empty excel files via os.remove(str(stocks[j]) + '.xlsx')
cleaning = True
dummy_counter = []
stock_symbols = []
rat = 'atk'
j = 0

while cleaning == True:
    empty_check = str(keys[j])
    file_checked = str(keys[j]) + '.xlsx'
    file_reader = pd.read_excel(file_checked, 'Sheet1')
    reader_output = str(file_reader.shape)
    dummy_counter.append(rat)
    stock_symbols.append(empty_check)
    #print(stock_symbols)

    if reader_output == "(0, 7)":
        os.remove(file_checked)
        stock_symbols.remove(empty_check)
        dummy_counter.remove(rat)

    j = j + 1
    if j == len(values):
        cleaning = False

# reads selected files
reading = True
stock_vals = []
acronyms = []
j = 0

while reading == True:
    this_stock = str(keys[j]) + '.xlsx'
    ticker = str(keys[j])
    reader = pd.read_excel(this_stock, 'Sheet1')
    book = reader['Adj Close'].iloc[-1]
    page = round(book, 2)
    print(str(stock_symbols[j]) + ', $' + str(page))
    stock_vals.append(page)
    acronyms.append(ticker)

    j = j + 1
    if j == len(values):
        reading = False


print("Number of Securities: ", len(stock_vals))
print()
print("Security List: ", stock_symbols)
print()




# get the % change of all selected stocks
searching = True
name_changers = []
changers = []
openval = []
closeval = []
j = 0

while searching == True:
    docxl = str(stock_symbols[j]) + '.xlsx'
    docnoxl = str(stock_symbols[j])
    ds2 = pd.read_excel(docxl)
    closed_at = ds2['Adj Close']

    x0 = closed_at.first_valid_index()
    x1 = closed_at.last_valid_index()
    x_ini = closed_at[x0]
    x_fin = closed_at[x1]
    moneyball = str(x_ini)
    openval.append(moneyball)
    skrillaball = str(x_fin)
    closeval.append(skrillaball)

    face_the_changes = (x_fin - x_ini)/(abs(x_ini))
    #print(docnoxl, face_the_changes)
    changers.append(face_the_changes)
    name_changers.append(docnoxl)
    #print('\n\n')

    j = j + 1
    if j == len(stock_symbols):
        searching = False

cactusjack = True
n = 0
old_money = []
new_money = []
print("\n")


while cactusjack == True:
    print(codex[n])
    print(stock_vals[n])
    print()
    old_cash = float(codex[n]) * float(openval[n])
    money = str(old_cash)
    new_cash = float(codex[n]) * float(closeval[n])
    skrilla = str(new_cash)
    print("old cash: ", old_cash)
    print("new cash: ", new_cash)
    print()
    print()
    old_money.append(money)
    new_money.append(skrilla)
    n += 1
    if n == 28:
        cactusjack = False

print("old money: ", old_money)
print()
print("new money: ", new_money)
print()
print()


alternatives_ini = old_money[0:4]
alternatives_fin = new_money[0:4]
print(alternatives_ini)
print(alternatives_fin)

alternatives_sector_ini = 0.0
alternatives_sector_fin = 0.0

adding = True
x = 0
while adding == True:
    alternatives_sector_ini = alternatives_sector_ini + float(alternatives_ini[x])
    alternatives_sector_fin = alternatives_sector_fin + float(alternatives_fin[x])

    x += 1
    if x == 4:
        adding = False

alternatives_percent_change = (alternatives_sector_fin - alternatives_sector_ini) / alternatives_sector_ini
apc = round(alternatives_percent_change, 4)

print("beginning alternatives: $", alternatives_sector_ini)
print("ending alternatives: $", alternatives_sector_fin)
print("percent change: ", apc)
print()



tech_ini = old_money[4:8]
tech_fin = new_money[4:8]
print(tech_ini)
print(tech_fin)

tech_sector_ini = 0.0
tech_sector_fin = 0.0


adding = True
x = 0
while adding == True:
    tech_sector_ini = tech_sector_ini + float(tech_ini[x])
    tech_sector_fin = tech_sector_fin + float(tech_fin[x])

    x += 1
    if x == 3:
        adding = False

tech_percent_change = (tech_sector_fin - tech_sector_ini) / tech_sector_ini
tpc = round(tech_percent_change, 4)

print("beggining tech: $", tech_sector_ini)
print("ending tech: $", tech_sector_fin)
print("percent change: ", tpc)
print()


financials_ini = old_money[8:12]
financials_fin = new_money[8:12]
print(financials_ini)
print(financials_fin)

financials_sector_ini = 0.0
financials_sector_fin = 0.0

adding = True
x = 0
while adding == True:
    financials_sector_ini = financials_sector_ini + float(financials_ini[x])
    financials_sector_fin = financials_sector_fin + float(financials_fin[x])

    x += 1
    if x == 3:
        adding = False

financials_percent_change = (financials_sector_fin - financials_sector_ini) / financials_sector_ini
fpc = round(financials_percent_change, 4)

print("beginning financials: $", financials_sector_ini)
print("ending financials: $", financials_sector_fin)
print("percent change: ", fpc)
print()



hc_ini = old_money[12:16]
hc_fin = new_money[12:16]
print(hc_ini)
print(hc_fin)

hc_sector_ini = 0.0
hc_sector_fin = 0.0

adding = True
x = 0
while adding == True:
    hc_sector_ini = hc_sector_ini + float(hc_ini[x])
    hc_sector_fin = hc_sector_fin + float(hc_fin[x])

    x += 1
    if x == 3:
        adding = False

hc_percent_change = (hc_sector_fin - hc_sector_ini) / hc_sector_ini
hcpc = round(hc_percent_change, 4)


print("beginning health care: $", hc_sector_ini)
print("ending health care: $", hc_sector_fin)
print("percent change: ", hcpc)
print()


cg_ini = old_money[16:21]
cg_fin = new_money[16:21]
print(cg_ini)
print(cg_fin)

cg_sector_ini = 0.0
cg_sector_fin = 0.0


adding = True
x = 0
while adding == True:
    cg_sector_ini = cg_sector_ini + float(cg_ini[x])
    cg_sector_fin = cg_sector_fin + float(cg_fin[x])

    x += 1
    if x == 4:
        adding = False

cg_percent_change = (cg_sector_fin - cg_sector_ini) / cg_sector_ini
cgpc = round(cg_percent_change, 4)


print("beginning consumer goods: $", cg_sector_ini)
print("ending consumer goods: $", cg_sector_fin)
print("percent change: ", cgpc)
print()



industrials_ini = old_money[21:23]
industrials_fin = new_money[21:23]
print(industrials_ini)
print(industrials_fin)

industrials_sector_ini = 0.0
industrials_sector_fin = 0.0

adding = True
x = 0
while adding == True:
    industrials_sector_ini = industrials_sector_ini + float(industrials_ini[x])
    industrials_sector_fin = industrials_sector_fin + float(industrials_fin[x])

    x += 1
    if x == 1:
        adding = False

industrials_percent_change = (industrials_sector_fin - industrials_sector_ini) / industrials_sector_ini
ipc = round(industrials_percent_change, 4)


print("beginning industrials: $", industrials_sector_ini)
print("ending industrials: $", industrials_sector_fin)
print("percent change: ", ipc)
print()



energy_ini = old_money[23:27]
energy_fin = new_money[23:27]
print(energy_ini)
print(energy_fin)

energy_sector_ini = 0.0
energy_sector_fin = 0.0

adding = True
x = 0
while adding == True:
    energy_sector_ini = energy_sector_ini + float(energy_ini[x])
    energy_sector_fin = energy_sector_fin + float(energy_fin[x])

    x += 1
    if x == 3:
        adding = False

energy_percent_change = (energy_sector_fin - energy_sector_ini) / energy_sector_ini
epc = round(energy_percent_change, 4)


print("beginning energy: ", energy_sector_ini)
print("ending energy: ", energy_sector_fin)
print("percent change: ", epc)
print()



old_portfolio = 0.0
new_portfolio = 0.0
sex = True
k = 0

while sex == True:
    old_portfolio = old_portfolio + float(old_money[k])
    new_portfolio = new_portfolio + float(new_money[k])
    k += 1
    if k == 28:
        sex = False


print("old portfolio: ", str(old_portfolio))
print("new portfolio: ", str(new_portfolio))
print()

portfolio_change = (new_portfolio - old_portfolio)
print("portfolio change: $", portfolio_change)
print()
print()

fixed_income = 125325.41
liquid_held = 66586.66

hiscore = fixed_income + liquid_held + new_portfolio
print("total portfolio value: ", hiscore)
print()
print()


# create dictionary for stock values, sort
res = {name_changers[i]: changers[i] for i in range(len(stock_symbols))}
results = sorted(res.items(), key=lambda x: x[1], reverse=True)


# collect the gainers and losers into a list, and split
finding_gainers = True
gain_counter = 0
gainers = []
fainers = []

# gainers
while finding_gainers == True:
    gainers.append(results[gain_counter])

    if gain_counter == tops:
        finding_gainers = False
    gain_counter += 1



# split the lists
gain_names, gain_vals = zip(*gainers)
print("Top performers in time interval (via percent +/-): ", gain_names)
print("Their percentage changes: ", gain_vals)
print("\n")




# gainers
print("YOUR RESULTS:\n")
gainer_finder = True
j = 0
k = j + 1

while gainer_finder == True:
    docxl = str(gain_names[j]) + '.xlsx'
    name_of_doc = str(gain_names[j])
    print("Gainer " + str(k) + ", ", name_of_doc, ":")
    print("---------------")
    df2 = pd.read_excel(docxl)
    closeprice = df2['Adj Close']
    volume = df2['Volume']

    c0 = closeprice.first_valid_index()
    c1 = closeprice.last_valid_index()
    c_ini = closeprice[c0]
    c_fin = closeprice[c1]
    print("Initial Price: ${:.2f}".format(c_ini))
    print("Final Price: ${:.2f}".format(c_fin))
    print()

    delta_price = (c_fin - c_ini)/(abs(c_ini))
    delta_price_out = delta_price * 100
    print("% Price Change: {:.2f} percent".format(delta_price_out))
    print('\n\n')

    j = j + 1
    k = k + 1
    if j == len(gain_names):
        gainer_finder = False
