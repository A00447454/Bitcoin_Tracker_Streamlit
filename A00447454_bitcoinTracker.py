#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:36:25 2022

@author: sunarithakaranth
"""

import pandas as pd
import requests
import streamlit as st

st.title('Bitcoin Prices')


days = st.slider('Number of days: ', 1, 365)
currency = st.radio('Currency:', ('CAD', 'USD', 'INR'))

API_URL = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=cad&days=90&interval=daily'
payload = {'vs_currency': currency, 'days': days, 'interval': 'daily'}

r = requests.get(API_URL, payload)
if r.status_code == 200:
    data = r.json()


df = pd.DataFrame(data['prices'], columns=['Date', currency])

df['Date'] = pd.to_datetime(df['Date'], unit='ms')
df = df.set_index('Date')
price = df[currency].mean()




st.subheader("Price Tracker")
st.line_chart(df[currency])
st.write('Average Price during this time was {} {}'.format(price, currency))

