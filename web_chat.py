import streamlit as st
from query_openai import query_model
import os

assistent = str(os.getenv('assistant_id4'))
apik = str(os.getenv('api_key'))
apik_t = str(type(apik))
assist_t = str(type(assistent))
assist_pr = assistent + " " +assist_t
apik_pr = apik + " "+  apik_t

# Streamlit app title
st.title("KOIOS v7")
col1, col2 = st.columns([3, 1])

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
    st.write("assystent_pr: ", assist_pr)
    st.write("apik_pr: ", apik_pr)
    if prompt:
        instructions = "you chat with me. if you find nothing in the files, search internet"
        # assistant_type = "GPT3"
        response_ai, full_response, thread = query_model(prompt, instructions, assistent)
        with col1:
            st.write("Response:", response_ai)
            st.write("Full Response:", full_response)
            st.write("Thread Trace:", thread.id)
        # Display the response and thread ID
