import streamlit as st
import pandas as pd
import requests
import datetime

'''
# How much will your taxi cost?
'''

st.markdown('''
I will need some information to estimate how much your ride will cost.
''')

'''
## Please inform the following:
'''

d = st.date_input("1. date and time", datetime.datetime(2025,3,12))

'''
2. pickup location
'''

'''
3. dropoff location
'''

numb_passagers = st.slider("4. how many passangers?", 1, 4, 1)

'''
## Thanks! Your predicted fare is:
'''
