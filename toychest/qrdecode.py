from qrtools import QR
url = QR(filename='/home/jjacob/Downloads/easy/qr1.bmp')
out = url.data_to_string()[3:]
print out
