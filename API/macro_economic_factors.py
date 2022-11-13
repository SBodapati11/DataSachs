import requests
import csv
import pandas as pd
#Real GDP - Quarterly - 3 Months
#RGD per Capita - Quarterly - 3 Months - 1947
#Treasury Yield - 10 year 1953
#Federal Funds Interest Rate - 
#CPI
#Inflation
#Inflation Expectation
#Consumer Sentiment
#Retail Sales
#Durable Goods Orders
#Unemployment Rate
#Nonfarm Payroll

def real_gdp():
    url = 'https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey=AKOPFUROVWG0P483'
    r = requests.get(url)
    data = r.json()
    data = data['data']
    df = pd.DataFrame(data)
    return df

def treasury_yield():
    url = 'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity=10year&apikey=AKOPFUROVWG0P483'
    r = requests.get(url)
    data = r.json()
    data = data['data']
    df = pd.DataFrame(data)
    return df

def federal_funds_rate():
    url = 'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey=AKOPFUROVWG0P483'
    r = requests.get(url)
    data = r.json()
    data = data['data']
    df = pd.DataFrame(data)
    return df

def cpi():
    url = 'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey=AKOPFUROVWG0P483'
    r = requests.get(url)
    data = r.json()
    data = data['data']
    df = pd.DataFrame(data)
    return df

def inflation():
    url = 'https://www.alphavantage.co/query?function=INFLATION&apikey=AKOPFUROVWG0P483'
    r = requests.get(url)
    data = r.json()
    data = data['data']
    df = pd.DataFrame(data)
    return df


def unemployment():
    url = 'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey=AKOPFUROVWG0P483'
    r = requests.get(url)
    data = r.json()
    data = data['data']
    df = pd.DataFrame(data)
    return df
 
real_gdp().to_csv('real_gdp.csv')
treasury_yield().to_csv('treasury_yield.csv')
federal_funds_rate().to_csv('federal_funds_rate.csv')
cpi().to_csv('cpi.csv')
inflation().to_csv('inflation.csv')
unemployment().to_csv('unemployment.csv')

#print(df.head(10))
