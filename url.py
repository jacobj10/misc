import requests
from qrtools import QR
out = "REDACTED"
while True:
	print "http://REDACTED/{0}.png".format(str(out))
	img_data = requests.get("http://REDACTED/{0}.png".format(out)).content
	with open('image_name.png', 'wb') as handler:
		handler.write(img_data)
	url = QR(filename='image_name.png')
	if url.decode():
		out = url.data_to_string()[3:]
