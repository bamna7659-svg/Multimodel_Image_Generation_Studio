import streamlit as st
from utils.chatbot import ask_ai


def faq_page():

    st.title("❓ Frequently Asked Questions")

    st.markdown("### Common Questions")

    with st.expander("🖼 How do I generate an image?"):
        st.write(
            "Go to Generate Image, enter your prompt, choose style and click Generate Image."
        )

    with st.expander("🎨 Which art styles are available?"):
        st.write(
            "Realistic, Anime, Cartoon, Oil Painting, Sketch, Fantasy and 3D Render."
        )

    with st.expander("📥 Can I download my generated images?"):
        st.write(
            "Yes. Click the Download Image button after the image is generated."
        )

    with st.expander("📜 Is image history saved?"):
        st.write(
            "Yes. Every generated image is saved in the History page."
        )

    st.markdown("---")

    st.subheader("🤖 Ask AI")

    question = st.text_input(
        "Ask anything about this application",
        placeholder="Example: Which prompt gives better quality?"
    )

    if st.button("💬 Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                try:
                    answer = ask_ai(question)
                    st.success("AI Response")
                    st.write(answer)

                except Exception as e:
                    st.error(f"Error: {e}")