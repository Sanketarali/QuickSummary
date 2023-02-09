import wikipedia as wiki
import streamlit as st

st.title("Wikipedia Article Summarizer")

query = st.text_input("Enter a search query:")
if st.button("Submit"):
    st.write("Summary:", wiki.summary(query))
