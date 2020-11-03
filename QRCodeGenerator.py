#pip install qrcode
#pip install pillow
import qrcode
import os

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)

title = input("Inserisci il nome dell'immagine: \t")
data = input("Inserisci i dati: \t")

qr.add_data(data)

qr.make(fit=True)
#fill_color cambia il colore del QRCdoe #back_color cambia il colore dello sfondo
img = qr.make_image(fill_color="black", back_color="white")  

os.chdir("QRCodeImages")    #Entrare nella cartella QRCodeImages
img.save(f"{title}.png")    #Creazione del QRCode nella cartella QRCodeImages

