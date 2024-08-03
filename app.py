import streamlit as st
import openai

# Streamlit secrets에서 API 키 불러오기
openai.api_key = st.secrets["openai"]["api_key"]

st.title('Simple Writing Service')

# 제목 입력
title = st.text_input('Enter a title')

# 버튼 클릭 시 동작
if st.button('Generate Text'):
    if title:
        with st.spinner('Generating...'):
            response = openai.Completion.create(
                engine="gpt-4o-mini",
                prompt=f"Write a short paragraph about: {title}",
                max_tokens=150
            )
            result = response.choices[0].text.strip()
            st.write(result)
    else:
        st.error('Please enter a title')
