import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title = "Command page",
    page_icon = "👋",
    layout="centered"
)

openai_api_key = ""

st.title('명령어를 입력해주세요')

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''

input = st.text_input("command")

if input:
    st.session_state['user_input'] = input

st.write("입력 정보: ", st.session_state['user_input'])

if st.button("fig4_test"):
    con = st.container()
    switch_page("fig4_test")

if st.button("fig4_test_1"):
    con = st.container()
    switch_page("fig4_test_1")

if st.button("fig4_test_2"):
    con = st.container()
    switch_page("fig4_test_2")

if st.button("fig4_test_3"):
    con = st.container()
    switch_page("fig4_test_3")

if st.button("fig4_test_4"):
    con = st.container()
    switch_page("fig4_test_4")

