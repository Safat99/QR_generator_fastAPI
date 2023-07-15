import qrcode
url = "https://qr-code-generator-t629.onrender.com/main"
qr = qrcode.make(url)
qr_image_path = "finalQR.png"
qr.save(qr_image_path)
