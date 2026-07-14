import streamlit as st
import os
from PIL import Image
from utils.helpers import load_history


def history_page():

    st.title("📜 Image Generation History")

    history = load_history()

    if not history:
        st.info("No history available.")
        return

    for index, item in enumerate(reversed(history)):

        st.container()

        col1, col2 = st.columns([1, 2])

        with col1:

            image_path = item.get("image_path")

            if image_path and os.path.exists(image_path):

                image = Image.open(image_path)

                st.image(
                    image,
                    use_container_width=True
                )

            else:
                st.warning("Image not found.")

        with col2:

            st.markdown("### 📝 Prompt")
            st.write(item["prompt"])

            st.markdown(f"**🎨 Style:** {item['style']}")
            st.markdown(f"**📐 Aspect Ratio:** {item['aspect_ratio']}")
            st.markdown(f"**📅 Date:** {item['date']}")

            if image_path and os.path.exists(image_path):

                with open(image_path, "rb") as file:

                    st.download_button(
                        label="📥 Download",
                        data=file,
                        file_name=os.path.basename(image_path),
                        mime="image/png",
                        key=f"download_{index}"
                    )

        st.divider()