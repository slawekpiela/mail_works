import streamlit as st
from query_openai import query_model
import os
import uuid

from configuration import api_key, assistant_id, assistant_id3, assistant_id4, Models


# Function to initialize session-specific data
def initialize_session_data():
    print("data initialisation")

    try:
        thread_back != None
        st.write('pierwszy ruch w sesji', thread_back)
        st.session_state['user_data'] = {
            'prompt': '',
            'instructions': '',
            'thread': thread_back,
            'assistant': None
        }

    except:
        st.write("drugi ruch w sesji - brak thread back")
        st.session_state['user_data'] = {
            'prompt': '',
            'instructions': '',
            'thread': thread_back,
            'assistant': None
        }




# Initialize session data

initialize_session_data()

assistant = str(assistant_id3)  # str(os.getenv('assistant_id4'))

# draw the page
st.title("KOIOS v0.1")
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())

col1, col2 = st.columns([3, 1])

with col2:
    choice1 = st.radio("Wybierz model AI: ", ['GPT', 'Anton'])

# Example of handling other session-specific data
prompt = st.text_input("Prompt:")
instructions = 'You are an assistant'

if st.button('Send'):
    st.session_state['user_data']['prompt'] = prompt
    st.session_state['user_data']['instructions'] = instructions
    st.session_state['user_data']['assistant'] = assistant
    st.subheader("after sent pressed: ", st.session_state['session_id'])

#First time. no thread ID
if st.session_state['user_data']['prompt'] and st.session_state['user_data']['thread']:
    st.write("id sesji2: ", st.session_state['session_id'])

    response_ai, full_response, thread_back = query_model(
        st.session_state['user_data']['prompt'],
        st.session_state['user_data']['instructions'],
        st.session_state['user_data']['assistant'],
        st.session_state['user_data']['thread'],
    )
    st.write("first time thread from query_model: ", st.session_state['user_data']['thread'])
#each consecutive time there is thread id - which means query_model procedure has been called before.
else:
    st.write("id sesji2: ", st.session_state['session_id'])
    st.write("taki thread id podano do query model: ", st.session_state['user_data']['thread'])
    response_ai, full_response, thread_back = query_model(
        st.session_state['user_data']['prompt'],
        st.session_state['user_data']['instructions'],
        st.session_state['user_data']['assistant'],
        st.session_state['user_data']['thread'],
    )


    st.write("taki otrzymano z query model", thread_back)
    with col1:
        st.write("Response:", response_ai)
    st.write("Thread Trace:", st.session_state['user_data']['thread'])
