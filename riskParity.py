import requests
import warnings
import pandas as pd

warnings.filterwarnings("ignore")

assets_data = {}

# Get the data for each asset
def get_data(assets):
    for asset in assets:
        atr_data, price_data = get_json(asset)
        assets_data[asset] = {'atr': atr_data, 'daily': price_data}

# Get the data from an API call given an asset
def get_json(asset):
    atr_url = f"https://www.alphavantage.co/query?function=ATR&symbol={asset}&interval=daily&time_period=14&apikey=8AZWAOQ0LHYGQMJ2"
    atr_response = requests.get(atr_url)
    atr_json = atr_response.json()
    
    price_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={asset}&apikey=8AZWAOQ0LHYGQMJ2"
    price_response = requests.get(price_url)
    price_json = price_response.json()
    return [atr_json, price_json]

# Gets the percent volatility of an asset by finding the Average True Range (ATR) values of the
# the asset and then dividing the ATR by the dollar value
# Data points are taken as in daily intervals over 14 periods (3 weeks)
def get_volatility(asset):
    # Get the most recent ATR of the given asset
    atr_json = assets_data[asset]['atr']
    date = atr_json['Meta Data']['3: Last Refreshed']
    atr = atr_json['Technical Analysis: ATR'][date]['ATR']

    # Get the most recent closing price of the given asset
    price_json = assets_data[asset]['daily']
    price = price_json['Time Series (Daily)'][date]['5. adjusted close']

    # Calculate the percent ATR of the given asset
    pct_atr = float(atr) / float(price)
    return pct_atr

# Get the covariance matrix which measures if there is a possible relationship between each stock
def get_correlation(assets):
    data = pd.DataFrame()
    for asset in assets:
        data[asset] = pd.to_numeric(pd.DataFrame(assets_data[asset]['daily']['Time Series (Daily)']).transpose()['5. adjusted close'])
    data.index = pd.to_datetime(data.index)
    return data.corr(method='pearson')

# Calculate the risk of the Risk Parity Portfolio or the Effective Number of Correlated Bets
def calculate_portfolio_risk(portfolio):
    portfolio_risk = 0
    assets = list(portfolio.keys())
    get_data(assets)
    weights = []
    correlation_matrix = get_correlation(assets)
    
    # Loop through the assets and calculate each asset's contribution and correlation component
    for i in range(len(assets)):
        asset = assets[i]
        volatility = get_volatility(asset)
        contribution = (portfolio[asset]) ** 2 + (volatility) ** 2
        correlation_component = 0
        for j in range(i+1, len(assets)):
            correlation_component += portfolio[asset] * portfolio[assets[j]] * correlation_matrix.iloc[j,i]
        portfolio_risk += contribution
        portfolio_risk += correlation_component
        weights.append({'contribution': contribution, 'correlation component': correlation_component})
    return [portfolio_risk, weights]

# Return the ideal weights 
def return_weights(weights, risk):
    result = []
    for i in range(len(weights)):
        result.append((weights[i]['contribution'] + weights[i]['correlation component']) / risk)
    return result

risk, variables = calculate_portfolio_risk({'GS': 0.5, 'IBM': 0.5})
weights = return_weights(variables, risk)
print(risk)
print(weights)