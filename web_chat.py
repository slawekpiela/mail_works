import streamlit as st
from query_openai import query_model
import os
import uuid

assistant = str(os.getenv('assistant_id4'))

# Streamlit app title
st.title("KOIOS v0.1")

# Initialize or retrieve the session ID
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())

# Display the session ID
st.write(f"Session ID: {st.session_state['session_id']}")

col1, col2 = st.columns([3, 1])

# Text input for prompt
prompt = st.text_input("Prompt:", "")

with col1:
    st.write("Response:", "")
    #st.write("Full Response:", "")
    st.write("Thread Trace:", "")

with col2:
    choice1 = st.radio("Wybierz model AI: ", ['GPT', 'Anton'])

# Button to submit prompt
if st.button("Submit"):
    if prompt:
        instructions = "you chat with me. if you find nothing in the files, search internet"

        response_ai, full_response, thread = query_model(prompt, instructions, assistant)
        with col1:
            st.write("Response:", response_ai)
            #st.write("Full Response:", full_response)
            st.write("Thread Trace:", thread.id)
