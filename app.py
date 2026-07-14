import streamlit as st
import os

from utils.theme import apply_theme

from components.navbar import show_sidebar
from components.home import home
from components.generate_image import image_generator
from components.gallery import gallery_page
from components.history import history_page
from components.how_to_use import how_to_use
from components.faqs import faq_page
from components.about_developer import about_developer
from components.footer import footer


# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Multimodal Image Generation Studio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ----------------------------
# Load Custom CSS
# ----------------------------
def load_css():

    css_file = os.path.join("assets", "css", "style.css")

    if os.path.exists(css_file):

        with open(css_file, "r", encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )


load_css()


# ----------------------------
# Sidebar Navigation
# ----------------------------
page = show_sidebar()

# Apply Theme
apply_theme()


# ----------------------------
# Pages
# ----------------------------
if page == "🏠 Home":
    home()

elif page == "🖼 Generate Image":
    image_generator()

elif page == "🖼 Gallery":
    gallery_page()

elif page == "📜 History":
    history_page()

elif page == "📖 How To Use":
    how_to_use()

elif page == "❓ FAQs":
    faq_page()

elif page == "👩‍💻 About Developer":
    about_developer()


# ----------------------------
# Footer
# ----------------------------
footer()