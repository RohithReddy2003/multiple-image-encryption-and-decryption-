import streamlit as st
from PIL import Image
import io
from Encryption import encrypt

def Multiple_Image():
    def fill_image_with_images(result_size, uploaded_files):
        # Create an empty image of the specified size with a grayscale mode
        result_image = Image.new("L", result_size, 0)

        # Initialize starting coordinates
        x, y, z = 0, 0, 0

        for uploaded_file in uploaded_files:
            # Open the image from BytesIO and convert to grayscale if not already
            img = Image.open(io.BytesIO(uploaded_file.read())).convert("L")

            # Check if the image can fit in the remaining space
            if x + img.width > result_size[0]:
                # If not, move to the next row and reset x coordinate
                if x == 0:
                    break
                x = 0
                y += z

            if y + img.height > result_size[1]:
                break

            # Paste the image onto the result image
            result_image.paste(img, (x, y))

            # Updating coordinates for the next image
            x += img.width
            if img.height > z:
                z = img.height

        return result_image

    # Streamlit UI
    st.markdown("## Encryption")
    st.markdown("Upload images one by one and click on encrypt button.")

    # Create a file uploader for multiple files
    uploaded_files = st.file_uploader("Choose multiple image files", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="file_uploader")
    st.image(uploaded_files)

    # Create a button to trigger the image composition
    button_clicked = st.button("Encrypt the images", key="compose_button")

    if button_clicked and uploaded_files:
        # Run the function
        result_image = fill_image_with_images((512, 512), uploaded_files)
        #st.image(result_image, caption='Result Image', use_column_width=True)
        # Save the result_image
        result_image.save(r"C:\Users\ROHITH\Downloads\result_image.png")
        encrypt()