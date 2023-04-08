import streamlit as st
import time

col1, col2, col3 = st.columns([1,2,1])
                             
col1.markdown(" # Welcome to my app!")
col1.markdown(" Here is some info on the app")

uploaded_photo = col2.file_uploader("upload a photo")
camera_photo = col2.camera_input("Take a photo")
col3.metric(label="Temperature", value="60 deg C", delta = "3 deg C")
progress_bar = col2.progress(0)
for perc_completed in range(100):
  time.sleep(0.05)
  progress_bar.progress(perc_completed+1)

col2.success("Photo uploaded successfully")

with st.expander("Click to read more"):
  st.write("Hello, here are more details.")
  if uploaded_photo is None:
    st.image(camera_photo)
  else:
    st.image(uploaded_photo)
     
