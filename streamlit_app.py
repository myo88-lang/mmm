import streamlit as st
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import pandas as pd
import mplfinance as mpf
import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"

st.image("https://www.istockphoto.com/jp/%E3%82%B9%E3%83%88%E3%83%83%E3%82%AF%E3%83%95%E3%82%A9%E3%83%88/%E6%97%A5%E6%9C%AC%E3%81%AE%E7%A6%8F%E5%B2%A1%E5%B8%82%E3%81%AE%E9%A2%A8%E6%99%AF-gm1491666938-515942820", caption="Scenery", use_container_width=True)
st.subheader("About Us")
st.write("We are dedicated to helping you make informed investment decisions.")
st.subheader("Services")
st.write("- Investment analysis")
st.write("- Portfolio management")
st.write("- Market insights")

st.subheader("Contact Us")
st.write("Get in touch to learn more about our services.")
# Specify title and logo for the webpage.
# Set up your web app
st.set_page_config(layout="wide", page_title="WebApp_Demo")

# Sidebar
st.sidebar.title("Input")
symbol = st.sidebar.text_input('Stock symbol: ', 'NVDA').upper()
ma1 = st.sidebar.slider('Short-term moving average days: ',min_value=10, max_value=100, step=10)
ma2 = st.sidebar.slider('Long-term moving average days: ',min_value=50, max_value=200, step=10)
# Selection for a specific time frame.
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date',value=datetime.date(2021,1,1))
with col2:
    edate = st.date_input('End Date',value=datetime.date.today())


st.title(f"Symbol : {symbol}")

stock = yf.Ticker(symbol)
if stock is not None:
  # Display company's basics
  st.write(f"# Name : {stock.info['shortName']}")
  st.write(f"# Market : {stock.info['market']}")
else:
  st.error("Failed to fetch historical data.")

data = yf.download(symbol,start=sdate,end=edate,multi_level_index=False,auto_adjust=False)
if data is not None:
    fig, ax = mpf.plot(data,type='candle',style='yahoo',mav=(ma1,ma2),volume=True,returnfig=True)
    st.pyplot(fig)
else:
    st.error("Failed to fetch historical data.")
