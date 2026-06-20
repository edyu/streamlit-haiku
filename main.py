import streamlit as st

from backend.hub import Hub
from frontend.pages import pages

if 'hub' not in st.session_state:
    st.session_state.hub = Hub()

if 'logged_in' in st.session_state and st.session_state.logged_in:
    page = st.navigation([pages['home'], pages['logout']])
else:
    page = st.navigation([pages['login'], pages['signup']])

page.run()

# st.title('Haiku Haven')

# database = Database()
# query_results = database.execute_query('SELECT * FROM haikus')
# st.write(query_results)
