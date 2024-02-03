import qrcode

# Function to generate QR code for a web link
def generate_qrcode(url, output_file="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

if __name__ == "__main__":
    web_link = "https://acses-links.netlify.app/"  # Replace with your web link
    output_filename = "acses-links.png"  # Specify the desired output filename

    generate_qrcode(web_link, output_filename)
    print(f"QR code generated and saved as {output_filename}")
