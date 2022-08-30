import qrcode
from PIL import Image, ImageDraw, ImageFont

input_data = "https://mitranail.planovin.com/#/"
qr = qrcode.QRCode(
    version=3,
    border=4
)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black")
img.save(r"C:\Users\shiva.ghanbari\Desktop\QR_MitraNail.png")
img = Image.open(r"C:\Users\shiva.ghanbari\Desktop\QR_MitraNail.png")
draw = ImageDraw.Draw(img)
txt = 'MitraNail'
font = ImageFont.truetype('arial.ttf', 30)
draw.text((100, 1), txt, font=font, fill=(204, 255, 255))
img.save(r"C:\Users\shiva.ghanbari\Desktop\QR_MitraNail.png")
