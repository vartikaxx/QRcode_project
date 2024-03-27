import qrcode

print("Let us generate QR code!!!")

code=input("Input text, link or data to create its QR code")
img=qrcode.make(code)
img.save("image.png") 
print("QR Code has been generated and saved as png image!")