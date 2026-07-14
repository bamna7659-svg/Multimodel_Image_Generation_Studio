import streamlit as st


def show_sidebar():

    st.sidebar.title("🎨 Multimodal Image Generation Studio")

    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "📌 Navigation",
        [
            "🏠 Home",
            "🖼 Generate Image",
            "🖼 Gallery",
            "📜 History",
            "📖 How To Use",
            "❓ FAQs",
            "👩‍💻 About Developer"
        ]
    )

    st.sidebar.markdown("---")

    # Theme Selection
    theme = st.sidebar.radio(
        "🎨 Theme",
        [
            "🌙 Dark",
            "☀️ Light"
        ]
    )

    # Save theme in session
    st.session_state["theme"] = theme

    st.sidebar.markdown("---")

    st.sidebar.success("🚀 AI Powered")

    st.sidebar.caption("Version 1.0")

    return page