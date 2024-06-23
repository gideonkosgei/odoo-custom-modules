import base64
import qrcode

def generate_qr_code(data):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    qr_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return qr_image_base64
