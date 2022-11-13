import requests



def extract_stocks():
    stock_symbols = ['GS', 'IBM', 'NFLX', 'MKTX', 'ABMD', 'TDG', 'AVGO', 'ALGN', 'URI', 'AMZN', 'ULTA']
    stock_data = []
    for stock in stock_symbols:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&outputsize=full&apikey=AKOPFUROVWG0P483"
        r = requests.get(url)
        data = r.json()
        stock_data.append(data)
    return stock_symbols


#url_2 = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'
#r = requests.get(url_2)
#data_2 = r.json()

#print(data_2)