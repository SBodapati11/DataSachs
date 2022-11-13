import pandas as pd
import numpy as np
from datetime import datetime



df_spx = pd.read_csv('SPX.csv')
df_spx = df_spx.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1)
df_spx['Year'] = pd.DatetimeIndex(df_spx['Date']).year
df_spx = df_spx.drop('Date', axis=1)
#df_spx.set_index('Year', inplace=True)
df_spx = df_spx.loc[df_spx['Year'] >= 2000]
df_spx = df_spx.reset_index(drop=True)
df_spx['Adj Close'] = df_spx['Adj Close'].diff()
#print(df_spx.head())

#df_cpi = pd.read_csv('cpi.csv')
#df_cpi = df_cpi.drop('Unnamed: 0', axis=1)
#df_cpi = df_cpi.rename(columns = {'date':'Date'})
#df_cpi = df_cpi.rename(columns = {'value':'cpi'})
#df_cpi['Year'] = pd.DatetimeIndex(df_cpi['Date']).year
#df_cpi = df_cpi.drop('Date', axis=1)
#df_cpi = df_cpi.loc[df_cpi['Year'] >= 2000]
#df_cpi = df_cpi.reset_index(drop=True)
#print(df_cpi.head())

#df_c = pd.merge(df_spx, df_cpi, how='outer', on='Year')

#print(df_c.head())

df_interest = pd.read_csv('federal_funds_rate.csv')
df_interest = df_interest.drop('Unnamed: 0', axis=1)
df_interest = df_interest.rename(columns = {'date':'Date'})
df_interest = df_interest.rename(columns = {'value':'interest'})
df_interest['Year'] = pd.DatetimeIndex(df_interest['Date']).year
df_interest = df_interest.drop('Date', axis=1)
df_interest = df_interest.loc[df_interest['Year'] >= 2000]

#df_interest = df_interest.reset_index(drop=True)
print(df_interest.head())

df_c = pd.merge(df_spx, df_interest, how='outer', on='Year')
#print(df_c.head())

df_inflation= pd.read_csv('inflation.csv')
df_inflation = df_inflation.drop('Unnamed: 0', axis=1)
df_inflation = df_inflation.rename(columns = {'date':'Date'})
df_inflation = df_inflation.rename(columns = {'value':'inflation'})
df_inflation['Year'] = pd.DatetimeIndex(df_inflation['Date']).year
df_inflation = df_inflation.drop('Date', axis=1)
df_inflation = df_inflation.loc[df_inflation['Year'] >= 2000]
#df_inflation = df_inflation.reset_index(drop=True)
print(df_inflation.head())
df_c = pd.merge(df_c, df_inflation, how='outer', on='Year')

df_gdp = pd.read_csv('real_gdp.csv')
df_gdp = df_gdp.drop('Unnamed: 0', axis=1)
df_gdp = df_gdp.rename(columns = {'date':'Date'})
df_gdp = df_gdp.rename(columns = {'value':'gdp'})
df_gdp['Year'] = pd.DatetimeIndex(df_gdp['Date']).year
df_gdp = df_gdp.drop('Date', axis=1)
df_gdp = df_gdp.loc[df_gdp['Year'] >= 2000]
#df_gdp = df_gdp.reset_index(drop=True)
print(df_gdp.head())
df_c = pd.merge(df_c, df_gdp, how='outer', on='Year')

df_yield = pd.read_csv('treasury_yield.csv')
df_yield = df_yield.drop('Unnamed: 0', axis=1)
df_yield = df_yield.rename(columns = {'date':'Date'})
df_yield = df_yield.rename(columns = {'value':'yield'})
df_yield['Year'] = pd.DatetimeIndex(df_yield['Date']).year
df_yield = df_yield.drop('Date', axis=1)
df_yield = df_yield.loc[df_yield['Year'] >= 2000]
#df_yield = df_yield.reset_index(drop=True)
print(df_yield.head())
df_c = pd.merge(df_c, df_yield, how='outer', on='Year')
print(df_c.head())

df_unemployment = pd.read_csv('unemployment.csv')
df_unemployment = df_unemployment.drop('Unnamed: 0', axis=1)
df_unemployment = df_unemployment.rename(columns = {'date':'Date'})
df_unemployment = df_unemployment.rename(columns = {'value':'unemployment'})
df_unemployment['Year'] = pd.DatetimeIndex(df_unemployment['Date']).year
df_unemployment = df_unemployment.drop('Date', axis=1)
df_unemployment = df_unemployment.loc[df_unemployment['Year'] >= 2000]

print(df_unemployment.head())
df_c = pd.merge(df_c, df_unemployment, how='outer', on='Year')
print(df_c.head())
df_c = df_c.drop_duplicates(subset=["Adj Close"], keep='first')
df_c = df_c.reset_index(drop=True)

df_c.to_csv('final_3.csv')