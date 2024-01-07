import streamlit as st

# Function to initialize session-specific data
def initialize_session_data():
    if 'user_data' not in st.session_state:
        # Initialize data specific to this session
        st.session_state['user_data'] = {
            'counter': 0,
            'other_data': None
        }

# Initialize session data
initialize_session_data()

# Display and increment a counter specific to each session
if st.button('Increment Counter'):
    st.session_state['user_data']['counter'] += 1

st.write(f"Session Counter: {st.session_state['user_data']['counter']}")

# Example of handling other session-specific data
user_input = st.text_input("Enter some data:")
if st.button('Update Data'):
    st.session_state['user_data']['other_data'] = user_input

if st.session_state['user_data']['other_data']:
    st.write(f"You entered: {st.session_state['user_data']['other_data']}")
