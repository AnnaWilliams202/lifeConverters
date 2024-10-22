import streamlit as st

def convert_to_km(miles):
    km = miles / 0.621371
    return km

def convert_to_ml(kilometers):
    mi = kilometers * 0.621371
    return mi



# Styled title just for experiment
st.markdown("<h1 style='text-align: center; color: salmon;'>Kilometers to Miles Converter 🌍</h1>", unsafe_allow_html=True)

conversion = st.radio('Choose the conversion:', ('KM to ML', 'ML to KM'))

input_value = st.number_input('Enter amount to convert', min_value=0.0)
button = st.button('Convert')

if conversion == 'KM to ML':
    if button:
        miles = convert_to_ml(input_value)
        st.success(f'{input_value} kilometers is equal to {miles:.2f} miles.')

elif conversion == 'ML to KM':
    if button:
        kilometers = convert_to_km(input_value)
        st.success(f'{input_value} miles is equal to {kilometers:.2f} kilometers.')