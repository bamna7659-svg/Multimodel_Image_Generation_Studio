import streamlit as st
from io import BytesIO

from utils.api import generate_image
from utils.helpers import random_prompt, save_history
from utils.image_downloader import save_image
from utils.prompt_enhancer import enhance_prompt


def image_generator():

    st.title("🎨 AI Image Generator")
    st.markdown("Create beautiful AI-generated artwork from your imagination.")

    prompt = st.text_area(
        "📝 Enter Your Prompt",
        placeholder="Example: A futuristic cyberpunk city at sunset, ultra realistic, 8K"
    )

    col1, col2 = st.columns(2)

    with col1:
        style = st.selectbox(
            "🎨 Art Style",
            [
                "Realistic",
                "Anime",
                "Cartoon",
                "Oil Painting",
                "Sketch",
                "Fantasy",
                "3D Render"
            ]
        )

    with col2:
        aspect_ratio = st.selectbox(
            "📐 Aspect Ratio",
            [
                "1:1",
                "16:9",
                "9:16",
                "4:3"
            ]
        )

    col3, col4 = st.columns(2)

    with col3:
        image_size = st.selectbox(
            "🖼 Image Size",
            [
                "512x512",
                "768x768",
                "1024x1024"
            ]
        )

    with col4:
        image_count = st.slider(
            "🔢 Number of Images",
            min_value=1,
            max_value=4,
            value=1
        )

    negative_prompt = st.text_input(
        "❌ Negative Prompt (Optional)",
        placeholder="Example: blurry, watermark, low quality"
    )

    col5, col6, col7 = st.columns(3)

    with col5:
        if st.button("🎲 Surprise Me"):
            st.info(random_prompt())

    with col6:
        if st.button("✨ Enhance Prompt"):
            if prompt.strip():
                enhanced = enhance_prompt(prompt, style)
                st.success(enhanced)
            else:
                st.warning("Please enter a prompt first.")

    with col7:
        generate = st.button("🚀 Generate Image")

    if generate:

        if prompt.strip() == "":
            st.warning("⚠️ Please enter a prompt.")
            return

        enhanced_prompt = enhance_prompt(prompt, style)

        final_prompt = f"""
Style: {style}
Aspect Ratio: {aspect_ratio}
Image Size: {image_size}
Negative Prompt: {negative_prompt}

Prompt:
{enhanced_prompt}
"""

        with st.spinner("🎨 Generating AI Image..."):

            try:

                image = generate_image(final_prompt)

                image_path = save_image(image)

                save_history(
                    prompt,
                    style,
                    aspect_ratio,
                    image_path
                )

                st.success("✅ Image Generated Successfully!")

                st.image(
                    image,
                    caption="Generated Image",
                    use_container_width=True
                )

                img = BytesIO()
                image.save(img, format="PNG")

                st.download_button(
                    label="📥 Download Image",
                    data=img.getvalue(),
                    file_name="generated_image.png",
                    mime="image/png"
                )

            except Exception as e:
                st.error(f"❌ {e}")