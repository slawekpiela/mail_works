import streamlit as st
import uuid

def main():

    # Initialize a unique session ID if it doesn't already exist
    if 'session_id' not in st.session_state:
        st.session_state['session_id'] = str(uuid.uuid4())

    # Initialize another session-specific variable
    if 'my_session_variable' not in st.session_state:
        st.session_state['my_session_variable'] = 'initial_value'

    # Display and modify the session-specific variable
    st.write(f"Session ID: {st.session_state['session_id']}")
    st.write(f"Current value of session variable: {st.session_state['my_session_variable']}")

    new_value = st.text_input("Enter a new value for the session variable")
    if st.button("Update"):
        st.session_state['my_session_variable'] = new_value
        st.write(f"Updated value of session variable: {st.session_state['my_session_variable']}")

if __name__ == "__main__":
    main()