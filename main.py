import qrcode
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Define the content of the QR code (e.g., URL or text)
content = "https://example.com"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(content)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

# Load the image
image_path = "invoice.jpg"  # Provide the path to your image
image = Image.open(image_path)

# Resize the image to fit within the QR code
qr_size = qr_image.size[0]
image = image.resize((qr_size, qr_size))

# Combine the QR code and the image
qr_image.paste(image, (0, 0))

# Create a blank canvas to add the wish note
canvas_width = qr_image.size[0]
canvas_height = qr_image.size[1] + 100  # Adjust the height as needed
canvas = Image.new("RGB", (canvas_width, canvas_height), "white")

# Paste the QR code onto the canvas
qr_position = ((canvas_width - qr_size) // 2, (canvas_height - qr_size) // 2)
canvas.paste(qr_image, qr_position)

# Add the wish note to the canvas
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype("/usr/share/fonts/truetype/tibetan-machine/TibetanMachineUni.ttf", 15)  # Provide the path to your font and adjust the size
wish_note = "With Love and blessings from MIE 16"  # Add your wish note here

# Calculate the size of the wish note text
text_bbox = draw.textbbox((0, 0), wish_note, font=font)
text_size = (text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1])

# Calculate the position to center the wish note
text_position = (
    (canvas_width - text_size[0]) // 2,
    qr_position[1] + qr_size + 10
)

# Draw the wish note text on the canvas
draw.text(text_position, wish_note, font=font, fill="black")

# Draw the wish note text on the canvas
draw.text(text_position, wish_note, font=font, fill="black")

# Save the QR code as an image file
qr_image_path = "path_to_save_qr_code.png"  # Provide the path to save the QR code image
canvas.save(qr_image_path)

# Print the QR code
# You can use a library like `qrcode_terminal` to print the QR code in the console:
# https://github.com/lincolnloop/python-qrcode#console-output
