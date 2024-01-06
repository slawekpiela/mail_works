import streamlit as st
import openai
from query_openai import query_model

# Streamlit app title
st.title("GPT-3 Assistant")

# Text input for prompt
prompt = st.text_input("Prompt:", "")

# Button to submit prompt
if st.button("Submit"):
    if prompt:
        instructions = "you chat with me. if you find nothing in the files, search internet"
        assistant_type = "GPT3"
        response_ai, full_response, thread = query_model(prompt, instructions, assistant_type)

        # Display the response and thread ID
        st.write("Response:", response_ai)
        st.write("Full Response:", full_response)
        st.write("Thread Trace:", thread.id)
