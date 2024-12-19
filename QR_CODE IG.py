import qrcode
from PIL import Image
link = ("https://www.instagram.com/zods666/")

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10, 
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr.code IG.png")