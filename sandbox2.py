import streamlit as st

# Initialize session state for storing appended text if it doesn't already exist
if 'appended_text' not in st.session_state:
    st.session_state['appended_text'] = ''

# Text input for new text
new_text = st.text_input("Enter text to append:")

# Button to append the text
if st.button("Append Text"):
    # Append new text to the existing text
    st.session_state['appended_text'] += new_text + '\n'  # Adding a newline for separation

# Display the appended text with red color using Markdown and HTML
st.markdown(f"<p style='color: red;'>{st.session_state['appended_text']}</p>", unsafe_allow_html=True)
