import qrcode
from PIL import Image, ImageDraw, ImageFont

input_data = "https://mitranail.planovin.com/#/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=3,
    border=4
)

# Add data to the QR code
qr.add_data(input_data)
qr.make(fit=True)

# Generate a QR code image
img = qr.make_image(fill_color="white", back_color="black")
img.save(r"C:\Users\shiva.ghanbari\Desktop\QR_MitraNail.png")
img = Image.open(r"C:\Users\shiva.ghanbari\Desktop\QR_MitraNail.png")

# Optionally, customize the QR code appearance using PIL
draw = ImageDraw.Draw(img)
txt = 'MitraNail'
font = ImageFont.truetype('arial.ttf', 30)
draw.text((100, 1), txt, fill=(204, 255, 255))
img.save(r"C:\Users\shiva.ghanbari\Desktop\QR_MitraNail.png")
