import streamlit as st


def how_to_use():

    st.title("📖 How To Use")
    st.markdown("Follow these simple steps to generate amazing AI images.")

    st.markdown("---")

    st.subheader("📝 Step 1: Enter Your Prompt")
    st.write(
        "Describe the image you want to generate. The more detailed your prompt, the better the result."
    )

    st.info("Example: A futuristic cyberpunk city at sunset, ultra realistic, 8K")

    st.markdown("---")

    st.subheader("🎨 Step 2: Select Art Style")
    st.write(
        "Choose your preferred art style such as Realistic, Anime, Cartoon, Fantasy, Sketch, Oil Painting or 3D Render."
    )

    st.markdown("---")

    st.subheader("📐 Step 3: Choose Aspect Ratio")
    st.write(
        "Select the aspect ratio that best suits your image."
    )

    st.markdown("---")

    st.subheader("🖼 Step 4: Select Image Size")
    st.write(
        "Choose the desired image resolution."
    )

    st.markdown("---")

    st.subheader("❌ Step 5: Add Negative Prompt (Optional)")
    st.write(
        "You can remove unwanted objects or improve image quality by adding a negative prompt."
    )

    st.info("Example: blurry, watermark, low quality")

    st.markdown("---")

    st.subheader("✨ Step 6: Enhance Prompt")
    st.write(
        "Click the 'Enhance Prompt' button to automatically improve your prompt before generating the image."
    )

    st.markdown("---")

    st.subheader("🚀 Step 7: Generate Image")
    st.write(
        "Click the Generate Image button and wait a few seconds while AI creates your artwork."
    )

    st.markdown("---")

    st.subheader("📥 Step 8: Download Image")
    st.write(
        "After the image is generated, click the Download button to save it to your device."
    )

    st.markdown("---")

    st.success("🎉 Enjoy creating beautiful AI-generated images!")