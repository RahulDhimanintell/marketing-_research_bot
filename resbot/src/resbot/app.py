import streamlit as st
from main import run
import crew


topic = st.text_input('Enter Companies Name')
result1, news = run(topic)
st.markdown('### Report')
st.write(result1)
st.markdown("### News")
st.write(news)