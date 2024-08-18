#importing all the necessary dependencies
from nselib import capital_market
from nselib import derivatives
from datetime import date, timedelta
import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import time 

#initializing streamlit config
st.set_page_config(
    page_title="NSE Stock Data Dashboard",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.title(':orange[NSE]Dashboard')
st.info("This is a NSE Data Analysing Dashboard", icon="💡")


#BankData = capital_market.price_volume_and_deliverable_position_data('SBIN', period='1M')
#st.dataframe(BankData)


#Different view options using multiselect
view_options = st.sidebar.multiselect("Select view option(s)", ["Block Deals", "Market Volatility","Short Selling Data", "Option Chain Data", "Option Price Volume Data"])
for view_option in view_options:
    st.subheader(f"{view_option}")
    if view_option == "Block Deals":
        #shows all the block deals data
        block_deals = capital_market.block_deals_data(period = '1M')
        st.dataframe(block_deals)

    elif view_option == "Market Volatility":
        #shows the volatility of the overall market 
        market_volatility = capital_market.india_vix_data(period='1M')
        st.dataframe(market_volatility)

    elif view_option == "Short Selling Data":
        #short selling data 
        short_selling_data = capital_market.short_selling_data(period='1M')
        st.dataframe(short_selling_data)

    elif view_option == "Option Chain Data":
        index_name = st.text_input("Enter index name", placeholder="Ex: BANKNIFTY")
        if index_name:
            try:
                option_chain_data = derivatives.nse_live_option_chain(index_name)
                st.dataframe(option_chain_data)
            except:
                st.error("Enter valid index name", icon="🚨")
        else:
            st.info("Enter Index name to view data", icon="ℹ️")

    elif view_option == "Option Price Volume Data":
        #live option price volume data
        option_price_volume_data = derivatives.option_price_volume_data('BANKNIFTY', 'OPTIDX',period='1M')
        st.dataframe(option_price_volume_data)


#Toggle switch for expiry dates view
show = st.sidebar.toggle("Show Expiry Dates")
if show:
    #expiry dates for option cjain index
    options_expiry = derivatives.expiry_dates_option_index()
    for key in options_expiry:
        st.sidebar.write(key, options_expiry[key])
        #for i in options_expiry[key]:
            #st.sidebar.write(i)

show_fii = st.sidebar.toggle("Show Foreign Investors Data")
if show_fii:
    try:
        #foreign institutional investors
        foreign_investors = derivatives.fii_derivatives_statistics('12-12-2023')
        st.write(foreign_investors)
    except:
        st.error("Could not fetch data: National Stock Exchange Server did not respond", icon="🚨")










