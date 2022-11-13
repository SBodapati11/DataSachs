import numpy as np
import streamlit as st
import yfinance as yf
import time

st.set_page_config(
    page_title="Personal Finance",
    page_icon="💰",
)

st.empty()

st.write("# Personal Finance 💰")
st.write("## Current Portfolio")

st.write("### Google")
# define ticker, get data
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
# get the start and end
tickerDf = tickerData.history(period='1d', start='2012-1-01', end='2022-1-01')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.line_chart(tickerDf.Close)


st.write("### Microsoft")
tickerSymbol = 'MSFT'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2012-1-01', end='2022-1-01')
st.line_chart(tickerDf.Close)


# Fake Portfolio

# Starting Investment:
starting_money = 100

st.write("### Your Portfolio")
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1) + starting_money
chart = st.line_chart(last_rows)

ending_money = starting_money

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("Loading Portfolio... %i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    ending_money = new_rows[-1]
    time.sleep(0.05)

progress_bar.empty()

st.write("### Starting Balance")
st.write(str(starting_money))
st.markdown("### Ending Balance")
st.write(str(ending_money[0]))

st.markdown("### Overall Change")
change = round(((ending_money[0] - starting_money)/abs(starting_money))*100, 2)

if change < 0:
    st.markdown(str(change) + "%")
else:
    st.markdown("+" + str(change) + "%")