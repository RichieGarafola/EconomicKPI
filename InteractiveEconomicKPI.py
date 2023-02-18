import pandas as pd
import pandas_datareader.data as web
import streamlit as st
import matplotlib.pyplot as plt
import datetime

# Set default start and end dates
default_start_date = pd.to_datetime('2010-01-01')
default_end_date = pd.to_datetime(datetime.date.today())

# Create a sidebar with options for economic indicators and date range
st.sidebar.title('Select Options')
indicator = st.sidebar.selectbox('Select Economic Indicator', ['Unemployment Rate', 'Consumer Price Index', 'Gross Domestic Product'])
start_date = st.sidebar.date_input('Start Date', default_start_date)
end_date = st.sidebar.date_input('End Date', default_end_date)

# Convert start and end dates to strings for data retrieval
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# Retrieve data for the selected economic indicator
if indicator == 'Unemployment Rate':
    data = web.DataReader('UNRATE', 'fred', start_date_str, end_date_str)
    title = 'US Unemployment Rate'
    ylabel = 'Percent'
elif indicator == 'Consumer Price Index':
    data = web.DataReader('CPALTT01USM657N', 'fred', start_date_str, end_date_str)
    title = 'US Consumer Price Index'
    ylabel = 'Index'
elif indicator == 'Gross Domestic Product':
    data = web.DataReader('GDP', 'fred', start_date_str, end_date_str)
    title = 'US Gross Domestic Product'
    ylabel = 'Trillions of Dollars'

# Create a dashboard to visualize the data
st.title('US Economic Indicators Dashboard')
st.write('Data Source: FRED')

# Plot the selected economic indicator
fig, ax = plt.subplots()
data.plot(ax=ax)
ax.set_title(title)
ax.set_xlabel('Year')
ax.set_ylabel(ylabel)
st.pyplot(fig)
