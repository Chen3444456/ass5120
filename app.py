import streamlit as st

st.title('Simple Streamlit App')

if st.button('Say hello'):
     st.write('Hello, World!')
else:
     st.write('Goodbye')
