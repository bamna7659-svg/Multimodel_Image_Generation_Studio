import streamlit as st

def home():

    st.title("🎨 Multimodal Image Generation Studio")

    st.subheader("Transform Your Imagination into AI Artwork")

    st.write("")

    st.info(
        "Generate high-quality AI images from simple text prompts."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### ✨ Features")

        st.write("✅ Text to Image")

        st.write("✅ Multiple Art Styles")

        st.write("✅ Download Images")

        st.write("✅ Image History")

        st.write("✅ AI Powered")

    with col2:

        st.markdown("### 🚀 Getting Started")

        st.write("1. Open Generate Image")

        st.write("2. Enter Prompt")

        st.write("3. Select Style")

        st.write("4. Generate")

        st.write("5. Download")

    st.markdown("---")

    st.header("🌟 Why Choose This Studio?")

    st.write("""
Our AI Studio converts your imagination into beautiful artwork
using modern AI Image Generation Models.
""")