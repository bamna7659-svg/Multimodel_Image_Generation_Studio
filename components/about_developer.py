import streamlit as st


def about_developer():

    st.title("👩‍💻 About Developer")

    st.markdown("""
    ## Hello! 👋

    Welcome to **Multimodal Image Generation Studio**.

    This project was developed by **Amna Bibi** as an AI-powered application that transforms text prompts into high-quality AI-generated images using modern Generative AI technologies.
    """)

    st.markdown("---")

    st.subheader("👤 Developer Information")

    st.write("**Name:** Amna Bibi")
    st.write("**Program:** BS Artificial Intelligence")
    st.write("**University:** Emerson University, Multan")
    st.write("**Status:** 6th Semester Completed")

    st.markdown("---")

    st.subheader("💻 Technical Skills")

    skills = [
        "🐍 Python",
        "🤖 Artificial Intelligence",
        "✨ Generative AI",
        "🎨 Streamlit",
        "🤗 Hugging Face",
        "⚡ Groq API",
        "🧠 Prompt Engineering",
        "🔗 Git & GitHub"
    ]

    for skill in skills:
        st.write(f"✅ {skill}")

    st.markdown("---")

    st.subheader("🌐 Connect With Me")

    st.markdown(
        """
        **🐙 GitHub**

        https://github.com/bamna7659-svg
        """
    )

    st.markdown(
        """
        **💼 LinkedIn**

        https://www.linkedin.com/in/amna-bibi-a0ba312b4
        """
    )

    st.markdown("---")

    st.success("⭐ Thank you for visiting my project!")

    st.info(
        "If you like this project, feel free to connect with me on GitHub and LinkedIn."
    )