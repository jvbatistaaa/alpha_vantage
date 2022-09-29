from requests import request
import pandas as pd

apikey = 'INSERT_API_KEY'
# Funções que fazem os requests dos dados da API
def get_crypto_intraday(symbol:str,market:str,interval:str):
    '''
    Retorna um JSON com as iformações sobre o tipo de ativo inserido como parâmetro
    symbol: BTC,ETH...
    market: USD,EUR,GBP...
    interval: 1min, 5min, 15min, 30min, 60min
    '''
    symbol = symbol.upper()
    market = market.upper()
    function = 'CRYPTO_INTRADAY'
    outputsize = 'full'
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&market={market}&interval={interval}&outputsize={outputsize}&apikey={apikey}'
    data = request('GET',url).json()
    prices = pd.DataFrame.from_dict(data[f'Time Series Crypto ({interval})'],orient='index')
    return prices
    

def get_crypto_daily(symbol:str,market:str):
    '''
    Retorna um DataFrame com as iformações sobre o ativo preços DIÁRIOS o-h-l-c, volume e Market Cap
    symbol: BTC,ETH...
    market: USD,EUR,GBP...
    '''
    symbol = symbol.upper()
    market = market.upper()
    function = 'DIGITAL_CURRENCY_DAILY'
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&market={market}&apikey={apikey}'
    data = request('GET',url).json()
    prices = pd.DataFrame.from_dict(data['Time Series (Digital Currency Daily)'],orient='index')
    return prices
   

def get_crypto_weekly(symbol:str,market:str):
    '''
    Retorna um JSON com as iformações sobre o ativo preços SEMANAIS o-h-l-c, volume e Market Cap
    symbol: BTC,ETH...
    market: USD,EUR,GBP...
    '''
    symbol = symbol.upper()
    market = market.upper()
    function = 'DIGITAL_CURRENCY_WEEKLY'
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&market={market}&apikey={apikey}'
    data = request('GET',url).json()
    print(data.keys())
    prices = pd.DataFrame.from_dict(data['Time Series (Digital Currency Weekly)'],orient='index')
    return prices

def get_crypto_monthly(symbol:str,market:str):
    '''
    Retorna um JSON com as iformações sobre o ativo preços MENSAIS o-h-l-c, volume e Market Cap
    symbol: BTC,ETH...
    market: USD,EUR,GBP...
    '''
    symbol = symbol.upper()
    market = market.upper()
    function = 'DIGITAL_CURRENCY_MONTHLY'
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&market={market}&apikey={apikey}'
    data = request('GET',url).json()

    prices = pd.DataFrame.from_dict(data['Time Series (Digital Currency Monthly)'],orient='index')
    return prices

def get_forex_intraday(from_symbol:str,to_symbol:str,interval:str):
    '''
    Retorna um JSON com as iformações sobre o ativo preços MENSAIS o-h-l-c, volume e Market Cap
    from_symbol: USD,EUR,GBP...
    to_symbol: USD,EUR,GBP...
    interval: 1min, 5min, 15min, 30min, 60min
    '''
    from_symbol = from_symbol.upper()
    to_symbol = to_symbol.upper()
    function = 'FX_INTRADAY'
    outputsize = 'full'
    url = f'https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&interval={interval}&outputsize={outputsize}&apikey={apikey}'
    data = request('GET',url).json()
    prices = pd.DataFrame.from_dict(data[f'Time Series FX ({interval})'],orient='index')
    return prices


def get_forex_daily(from_symbol:str,to_symbol:str):
    '''
    Retorna um JSON com as iformações sobre o ativo preços MENSAIS o-h-l-c, volume e Market Cap
    from_symbol: USD,EUR,GBP...
    to_symbol: USD,EUR,GBP...
    '''
    from_symbol = from_symbol.upper()
    to_symbol = to_symbol.upper()
    function = 'FX_DAILY'
    outputsize = 'full'
    url = f'https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize={outputsize}&apikey={apikey}'
    data = request('GET',url).json()
    prices = pd.DataFrame.from_dict(data['Time Series FX (Daily)'],orient='index')
    return prices

def get_forex_weekly(from_symbol:str,to_symbol:str):
    '''
    Retorna um JSON com as iformações sobre o ativo preços MENSAIS o-h-l-c, volume e Market Cap
    from_symbol: USD,EUR,GBP...
    to_symbol: USD,EUR,GBP...
    '''
    from_symbol = from_symbol.upper()
    to_symbol = to_symbol.upper()
    function = 'FX_WEEKLY'
    outputsize = 'full'
    url = f'https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize={outputsize}&apikey={apikey}'
    data = request('GET',url).json()
    prices = pd.DataFrame.from_dict(data['Time Series FX (Weekly)'],orient='index')
    return prices

def get_forex_monthly(from_symbol:str,to_symbol:str):
    '''
    Retorna um JSON com as iformações sobre o ativo preços MENSAIS o-h-l-c, volume e Market Cap
    from_symbol: USD,EUR,GBP...
    to_symbol: USD,EUR,GBP...
    '''
    from_symbol = from_symbol.upper()
    to_symbol = to_symbol.upper()
    function = 'FX_MONTHLY'
    outputsize = 'full'
    url = f'https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize={outputsize}&apikey={apikey}'
    data = request('GET',url).json()
    prices = pd.DataFrame.from_dict(data['Time Series FX (Monthly)'],orient='index')
    return prices
    

# Funções que retornam os nomes dos ativos
def get_crypto_symbols():
    '''
    This method returns the symbol of each Cryptocurrency avaiable in Alpha Vantage API
    '''
    with open('files/digital_currency_list.csv', 'r') as file:
        lst = []
        file.readline()
        for n in file:
            lst.append(n.split(',')[0])
    return lst

def get_physical_currencies():
    '''
    This method returns the symbol of each Physical Currency avaiable in Alpha Vantage API
    '''
    with open('files/physical_currency_list.csv', 'r') as file:
        lst = []
        file.readline()
        for n in file:
            lst.append(n.split(',')[0])
    return lst


