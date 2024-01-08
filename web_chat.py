import streamlit as st
from query_openai import query_model
import os
import uuid

from configuration import api_key, assistant_id, assistant_id3, assistant_id4, Models


# Function to initialize session-specific data
def initialize_session_data():
    if 'user_data' not in st.session_state:
        st.session_state['user_data'] = {
            'prompt': '',
            'instructions': '',
            'thread': '',
            'assistant': None
        }


initialize_session_data()

# Initialize session data

initialize_session_data()

assistant = str(assistant_id3)  # str(os.getenv('assistant_id4'))

# draw the page
st.title("KOIOS v0.1")
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())

col1, col2 = st.columns([3, 1])
with col1:
    st.write("Response:", "")
    # st.write("Full Response:", "")
    st.write("Thread Trace:", "")
with col2:
    choice1 = st.radio("Wybierz model AI: ", ['GPT', 'Anton'])

# Example of handling other session-specific data
prompt = st.text_input("Prompt:")
instructions = 'You are an assistant'


if st.button('Send'):
    st.session_state['user_data']['prompt'] = prompt
    st.session_state['user_data']['instructions'] = instructions
    st.session_state['user_data']['assistant'] = assistant

if st.session_state['user_data']['prompt']:
    response_ai, full_response, thread_from_query = query_model(
        st.session_state['user_data']['prompt'],
        st.session_state['user_data']['instructions'],
        st.session_state['user_data']['assistant'],
        st.session_state['user_data']['thread']
    )
    temp_thread = thread_from_query
    st.session_state['user_data']['thread'] = thread_from_query


    with col1:
        st.write("Response:", response_ai)
        st.write("Thread Trace:",  st.session_state['user_data']['thread'])
        st.write("TFQ: ",thread_from_query)

