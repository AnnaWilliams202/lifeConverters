import streamlit as st
import requests

# https://www.exchangerate-api.com
api_key = '0a19aa6149aaa510945d8412'
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'


def get_conversion_rates():
    response = requests.get(url)
    return response.json()['conversion_rates']


def convert_to_rub(amount_usd, conversion_rates):
    return amount_usd * conversion_rates['RUB']


def convert_to_usd(amount_rub, conversion_rates):
    return amount_rub / conversion_rates['RUB']


st.title('Life Currency Converter : "USD" to "RUB" ')
conversion = st.radio('Choose the conversion currency: ', ('USD to RUB', 'RUB to USD'))
input_value = st.number_input('Enter amount to convert', min_value=0.0)
button = st.button('Convert')

conversion_rates = get_conversion_rates()

if conversion == 'USD to RUB':
    if button:
        rubbles = convert_to_rub(input_value, conversion_rates)
        st.success(f"{input_value} USD is equal to {rubbles:.2f} RUB")

else:  # RUB to USD
    if button:
        dollars = convert_to_usd(input_value, conversion_rates)
        st.success(f"{input_value} RUB is equal to {dollars:.2f} USD")