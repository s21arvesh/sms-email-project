import pyqrcode

content="Cheers to 23 "

url = pyqrcode.create(content)

url.png("myqr.png",scale=5)

print("qr done successgully")