from streamlit import *
from rembg import remove
from PIL import Image

# Header with centered title
markdown(
    """
    <div style="text-align: center; font-size: 50px;">
        <strong>Background Remover</strong>
    </div>
    """,
    unsafe_allow_html=True
)

# File uploader
uploaded_file = file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open the uploaded image without altering the original
    input_image = Image.open(uploaded_file)

    # Resize the image only for display
    display_image = input_image.copy()
    display_image.thumbnail((300, 300))  # Resize the display image to max width/height of 300 pixels

    # Display the resized image
    image(display_image, caption="Uploaded Image (Display Only)", use_column_width=False)

    # Remove the background (keeping the original size)
    output_image = remove(input_image)

    # Display the background-removed image (for display purposes only, resize here as well)
    display_output_image = output_image.copy()
    display_output_image.thumbnail((300, 300))
    image(display_output_image, caption="Image with Background Removed (Display Only)", use_column_width=False)

    # Save the result for download (original resolution)
    output_file = "removed_bg.png"
    output_image.save(output_file, format="PNG")

    # Download link for the full-size image with removed background
    with open(output_file, "rb") as file:
        download_button(
            label="Download Image with Removed Background",
            data=file,
            file_name="removed_bg.png",
            mime="image/png"
        )
write("Developed by: Keith Renz")
