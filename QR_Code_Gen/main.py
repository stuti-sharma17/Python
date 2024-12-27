import qrcode
if __name__=='__main__':
    data=input('Enter the text or URL: ').strip()
    filename=input('Enter the filename : ').strip()
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make()
    img=qr.make_image(fill_color='black',back_color='white')
    img.save(filename)
    print(f'QR Code saved as {filename}')