import streamlit as st
from query_openai import query_model

# Streamlit app title
st.title("KOIOS v2")
col1, col2  = st.columns([3,1])

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
        assistant_type = "GPT3"
        response_ai, full_response, thread = query_model(prompt, instructions)
        with col1:
            st.write("Response:", response_ai)
            st.write("Full Response:", full_response)
            st.write("Thread Trace:", thread.id)
        # Display the response and thread ID
