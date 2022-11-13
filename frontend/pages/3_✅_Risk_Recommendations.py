import streamlit as st
import pandas as pd
from scipy.optimize import minimize
import requests
import warnings
import numpy as np

warnings.filterwarnings("ignore")

assets_data = {}

# Get the data for each asset
def get_data(assets):
    for asset in assets:
        atr_data, price_data = get_json(asset)
        assets_data[asset] = {'atr': atr_data, 'daily': price_data}

# Get the data from an API call given an asset
def get_json(asset):
    atr_url = f"https://www.alphavantage.co/query?function=ATR&symbol={asset}&interval=daily&time_period=14&apikey=0R8385RUA6UEHFCZ"
    atr_response = requests.get(atr_url)
    atr_json = atr_response.json()
    
    price_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={asset}&apikey=0R8385RUA6UEHFCZ"
    price_response = requests.get(price_url)
    price_json = price_response.json()
    return [atr_json, price_json]

get_data(["GS", "IBM"])
print(assets_data['GS']['daily']['Time Series (Daily)'])

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
def calculate_portfolio_risk(dollar_weights, assets):
    portfolio_risk = 0
    weights = []
    correlation_matrix = get_correlation(assets)
    
    # Loop through the assets and calculate each asset's contribution and correlation component
    for i in range(len(assets)):
        asset = assets[i]
        volatility = get_volatility(asset)
        contribution = (dollar_weights[i]) ** 2 + (volatility) ** 2
        correlation_component = 0
        for j in range(i+1, len(assets)):
            correlation_component += dollar_weights[i] * dollar_weights[j] * correlation_matrix.iloc[j,i]
        portfolio_risk += contribution
        portfolio_risk += correlation_component
        weights.append({'contribution': contribution, 'correlation component': correlation_component})
    return [assets, portfolio_risk, weights]

# Return the ideal weights 
def return_weights(weights, risk):
    result = []
    for i in range(len(weights)):
        result.append((weights[i]['contribution'] + weights[i]['correlation component']) / risk)
    return result

# Return the optimized dollar weights given equal risk weights
def return_optimized_weights(assets):
    sum_weights = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}
    bounds = ((0.0, 1.0),) * len(assets)

    # Internal function which calculates the mean squared error between the current weights and the optimal weights
    def mean_squared_error(weights, optimal_risk_weight):
        _, portfolio_risk, dollar_weight_contributions = calculate_portfolio_risk(weights, assets)
        weight_contributions = return_weights(dollar_weight_contributions, portfolio_risk)
        return ((weight_contributions - optimal_risk_weight) ** 2).sum()
    
    # Uses scipy.optimize to find the best dollar weights to have an equal risk
    optimal = np.repeat(1/len(assets), len(assets))
    optimal_weights = minimize(mean_squared_error, optimal,
                       args=(optimal), method='SLSQP',
                       options={'disp': False},
                       constraints=(sum_weights,),
                       bounds=bounds)
    return optimal_weights.x

assets, risk, variables = calculate_portfolio_risk([0.5, 0.5], ['GS', 'IBM'])
weights = return_weights(variables, risk)
optimal_weights = return_optimized_weights(assets)

st.set_page_config(
    page_title="Portfolio Risk Analysis"
)

st.title("Portfolio Risk Analysis")

st.subheader("Current Portfolio Dollar Weights")

risk_data_curr = {'Assets': assets, 'Weights': [0.5, 0.5]}
dollar_weights_curr = pd.DataFrame(risk_data_curr)
dollar_weights_curr.set_index('Assets', inplace=True)

st.bar_chart(dollar_weights_curr)

st.caption("These are the current dollar weightages of the assets in your portfolio.")
st.caption("In other words, this is how much of each stock you invested in your portfolio.")

st.subheader("Current Portfolio Risk Weights")

risk_data = {'Assets': assets, 'Weights': weights}
risk_weights = pd.DataFrame(risk_data)
risk_weights.set_index('Assets', inplace=True)

st.bar_chart(risk_weights)

st.caption("These are the current risk weightages of the assets in your portfolio.")
st.caption("In other words, this is how much each stock contributes to the overall risk of your portfolio.")

st.subheader("Optimal Portfolio Dollar Weights")

optimized_data = {'Assets': assets, "Weights": optimal_weights}
optimal_dollar_weights = pd.DataFrame(optimized_data)
optimal_dollar_weights.set_index('Assets', inplace=True)

st.bar_chart(optimal_dollar_weights)
st.caption("These are the optimal dollar weightages of the assets in your portfolio.")
st.caption("In other words, this is how much of each stock you should invest in your portfolio to balance the risk across your portfolio.")



