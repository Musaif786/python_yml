#from turtle import back, fillcolor
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=2)

qr.add_data("https://musaif.netlify.com")
qr.make(fit=True)
img=qr.make_image(fill_color='white',back_color='black')
img.save("Musaif_port.png")