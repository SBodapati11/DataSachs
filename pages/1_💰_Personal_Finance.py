import numpy as np
import streamlit as st
import yfinance as yf
import time
import pandas as pd

st.set_page_config(
    page_title="Personal Finance",
    page_icon="💰",
)

st.empty()

st.write("# Personal Finance 💰")
st.write("## Current Portfolio (01/01/2022)-(11/01/2022) ")

st.write("### Goldman Sachs (50%)")
# define ticker, get data
tickerSymbol = 'GS'
tickerData = yf.Ticker(tickerSymbol)
# get the start and end
gs_tickerDf = tickerData.history(period='1d', start='2022-01-01', end='2022-11-01')
gs_pct_returns = gs_tickerDf.Open.pct_change()
st.line_chart(gs_tickerDf.Close)

st.write("### IBM (50%)")
tickerSymbol = 'IBM'
tickerData = yf.Ticker(tickerSymbol)
ibm_tickerDf = tickerData.history(period='1d', start='2022-01-01', end='2022-11-01')
ibm_pct_returns = ibm_tickerDf.Open.pct_change()
st.line_chart(ibm_tickerDf.Close)

returns = pd.DataFrame({'GS Returns': gs_pct_returns[1:], 'IBM Returns': ibm_pct_returns[1:]})
weight = [0.5, 0.5]
weighted_returns = (weight * returns)
portfolio_returns = weighted_returns.sum(axis=1)

# Starting Investment:
starting_money = 10000

st.write("### Your Portfolio")
last_rows = [10000]

for i in range(len(portfolio_returns)):
    last_rows.append((portfolio_returns.iloc[i] * last_rows[-1]) + last_rows[-1])

ending_money = last_rows[-1]
portfolio_data = pd.DataFrame(last_rows[1:], index=portfolio_returns.index)
chart = st.line_chart(portfolio_data)

st.write("### Starting Balance")
st.write(str(starting_money))
st.markdown("### Ending Balance")
st.write(str(ending_money))

st.markdown("### Overall Change")
change = round(((ending_money - starting_money)/abs(starting_money))*100, 2)

if change < 0:
    st.markdown(str(change) + "%")
else:
    st.markdown("+" + str(change) + "%")