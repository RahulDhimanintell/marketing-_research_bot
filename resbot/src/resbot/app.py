import streamlit as st
from main import run
import crew
import asyncio

topic = st.text_input('Enter Companies Name')
async def stream():
    if topic:
        with st.spinner('Wait for it...'):
            result1, news = run(topic)
            st.markdown('### Report')
            st.write(result1)
            st.markdown("### News")
            st.write(news)
    else:
        pass


asyncio.run(stream())