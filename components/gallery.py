import streamlit as st
import os
from PIL import Image

IMAGE_FOLDER = "generated_images"


def gallery_page():

    st.title("🖼 Gallery")

    if not os.path.exists(IMAGE_FOLDER):
        st.info("No images found.")
        return

    images = [
        f for f in os.listdir(IMAGE_FOLDER)
        if f.endswith((".png", ".jpg", ".jpeg"))
    ]

    if len(images) == 0:
        st.info("No generated images yet.")
        return

    cols = st.columns(3)

    for index, image_name in enumerate(reversed(images)):

        image_path = os.path.join(IMAGE_FOLDER, image_name)

        with cols[index % 3]:

            image = Image.open(image_path)

            st.image(
                image,
                use_container_width=True
            )

            with open(image_path, "rb") as file:

                st.download_button(
                    "📥 Download",
                    data=file,
                    file_name=image_name,
                    mime="image/png",
                    key=image_name
                )