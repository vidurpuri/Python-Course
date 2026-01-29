import qrcode

url = 'https://pypi.org/project/qrcode/'
qrCode_filename = input('Enter filename (without extension): ')

if(qrCode_filename != ''):
    qrCode_filename += '.png'

img = qrcode.make(url)
img.save(qrCode_filename)