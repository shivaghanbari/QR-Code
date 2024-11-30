import qrcode
from PIL import Image, ImageDraw, ImageFont

input_data = "https://drive.google.com/file/d/1dF-wcbHNMO1l9NHZU_0l1d4SVPybPASb/view?usp=drive_link"

# Create a QR code instance
qr = qrcode.QRCode(
    version=3,
    border=4
)

# Add data to the QR code
qr.add_data(input_data)
qr.make(fit=True)

# Generate a QR code image (white and jet black)
img = qr.make_image(fill_color="white", back_color=(52, 52, 52))
img.save(r"C:\QR_HappyBD.png")
img = Image.open(r"C:\QR_HappyBD.png")

# Customize the QR code appearance using PIL
draw = ImageDraw.Draw(img)
txt = 'Dear ** scan me!'

# Load a font with sufficient thickness
font = ImageFont.truetype('arial.ttf', 25)

# Set text position in the top-left corner
x_position = 10  # Slight margin from the left edge
y_position = 10  # Slight margin from the top edge

# Colors for 3D effect
main_color = (255,255,255)    # main text

# 3D and Bold Effect: Draw shadow slightly offset
offset = 1  # Offset for the shadow effect
for x_off in range(-offset, offset + 1):
    for y_off in range(-offset, offset + 1):
        # Skip the main center position to avoid over-thickening
        if x_off == 0 and y_off == 0:
            continue
        draw.text((x_position + x_off, y_position + y_off), txt, font=font, fill=(53, 57, 53))

# Draw the main text in the desired color (light pink)
draw.text((x_position, y_position), txt, font=font, fill=main_color)

# Save the modified image
img.save(r"C:\QR_HappyBD.png")
