import streamlit as st

# Function to initialize session-specific data
def initialize_session_data():
    if 'user_data' not in st.session_state:
        # Initialize data specific to this session
        st.session_state['user_data'] = {
            'counter': 0,
            'prompt': None
        }

# Initialize session data
initialize_session_data()

col1, col2 = st.columns([3, 1])
with col1:
    st.write("Response:", "")
    #st.write("Full Response:", "")
    st.write("Thread Trace:", "")
with col2:
    choice1 = st.radio("Wybierz model AI: ", ['GPT', 'Anton'])




# Example of handling other session-specific data
prompt = st.text_input("Prompt:")
if st.button('Update Data'):
    st.session_state['user_data']['prompt'] = prompt



if st.session_state['user_data']['prompt']:
    st.write(f"You entered: {st.session_state['user_data']['prompt']}")
