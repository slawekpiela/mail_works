import streamlit as st
from query_openai import query_model
import os

assistant = str(os.getenv('assistant_id4'))

# Streamlit app title
st.title("KOIOS v0.1")
col1, col2 = st.columns([3, 1])

# Initialize session state for thread if it doesn't already exist
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = None

# Text input for prompt
prompt = st.text_input("Prompt:", "")

with col1:
    st.write("Response:", "")
    st.write("Full Response:", "")
    st.write("Thread Trace:", "")

with col2:
    choice1 = st.radio("Wybierz model AI: ", ['GPT', 'Anton'])

# Button to submit prompt
if st.button("Submit"):
    if prompt:
        instructions = "you chat with me. if you find nothing in the files, search internet"

        # Pass the existing thread ID (if any) to the query model
        response_ai, full_response, thread = query_model(prompt, instructions, assistant, st.session_state['thread_id'])

        # Update the session state with the new thread ID
        st.session_state['thread_id'] = thread.id if thread else None

        with col1:
            st.write("Response:", response_ai)
            st.write("Full Response:", full_response)
            st.write("Thread Trace:", thread.id if thread else "No thread")
