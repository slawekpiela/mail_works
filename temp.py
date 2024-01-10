import os

import streamlit as st
from configuration import assistant_id3
from query_openai import query_model
import uuid

# Initialize session-specific variables
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())
    st.write('pierwsze przypisanie sesji', st.session_state['session_id'])
    #os.environ[st.session_state['session_id']]= st.session_state['session_id']


if 'user_data' not in st.session_state:
    st.write("user_data_reset")
    st.session_state['user_data'] = {
        'prompt': '',
        'instructions': '',
        'thread':  os.getenv(st.session_state['session_id']),
        'assistant': None
    }

st.title("KOIOS v0.1")
col1, col2 = st.columns([3, 1])

# Main Function
def main():
    # Get user input
    prompt = st.text_input("Prompt:", key='prompt_input')

    # Handle button click
    if st.button('Send'):
        st.session_state['user_data']['prompt'] = prompt
        st.session_state['user_data']['assistant'] = str(assistant_id3)
        st.session_state['user_data']['instructions'] = 'be precise and concise'
        st.session_state['user_data']['thread'] = os.getenv(st.session_state['session_id'])

        # Call the query_model function with the updated session state
        response_ai, full_response,  thread_back = query_model(
            st.session_state['user_data']['prompt'],
            st.session_state['user_data']['instructions'],
            st.session_state['user_data']['assistant'],
            os.getenv(st.session_state['session_id'])
        )
        st.write("watek po odpytaniu modelu ", thread_back)
        # Display response and other data (optional)
        with col1:
            st.write("Response:", response_ai)
            os.environ[st.session_state['session_id']] = thread_back

    # Display session information
    st.write("Session ID:", st.session_state['session_id'], "os_var= ", os.getenv(st.session_state['session_id']))
    st.write("Thread ID:", st.session_state['user_data']['thread'])
    st.write("thread_back",  thread_back)
    os.environ[st.session_state['session_id']] = thread_back

if __name__ == "__main__":
    main()
