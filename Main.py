import streamlit as st
import storage.storage as storage
import utils.ui as ui
import utils.session as session

session.current_page("practice")

ui.load_css("main_style")

if "loaded" not in st.session_state:
    storage.load()
    st.session_state.loaded = True

st.markdown(
    """
    <div class="main-title" id="test">
        <h1 id="snoo">WELCOME TO CARDLET</h1>
        <p>An AI powered flashcard maker!</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-button">', unsafe_allow_html=True)

left, center, right = st.columns([1, 2, 1])

with center:
    if st.button("MANAGE", use_container_width=True):
        st.switch_page("pages/5_Manage.py")

    if st.button("PRACTICE", use_container_width=True):
        st.switch_page("pages/2_Practice.py")

st.markdown('</div>', unsafe_allow_html=True)
