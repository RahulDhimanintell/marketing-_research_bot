import streamlit as st
from main import run
import crew


topic = st.text_input('Enter topic')
result,result1 = run(topic)
st.write(result)
st.balloons
st.write(result1)