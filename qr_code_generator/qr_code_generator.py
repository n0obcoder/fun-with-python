# https://ourcodeworld.com/articles/read/554/how-to-create-a-qr-code-image-or-svg-in-python
import sys

def q(text=''):
    print(f'>{text}<')
    sys.exit() 

import qrcode

# create qrcode instance
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, 
                   box_size=10, border = 4)

data = 'this QR code generator works, bitch !'

# Add data to the qrcode instance
qr.add_data(data)

print('qr.__dict__: ', qr.__dict__)

# Make QR code (image) 
img = qr.make_image()
img.save('qr_fun.png')