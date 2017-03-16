import qrtools
import requests
d = qrtools.QR
url = "http://tunnel.web.easyctf.com/images/DaicO7460493nYSuvLPW.png"
x = requests.get(url).content
print(d(x).decode())
