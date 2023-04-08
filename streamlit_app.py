import streamlit as st

col1, col2, col3 = st.columns([1,2,1])
                             
col1.markdown(" # Welcome to my app!")
col1.markdown(" Here is some info on the app")

uploaded_phot = col2.file_uploader("upload a photo")
