import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

date = "https://resume-diwjiw.onrender.com/"
qr.add_data(date)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("Test.png")
