import qrcode

# Get user input
file_name = input("Name the QR Code (filename without extension): ").strip()
url = input("Insert URL: ").strip()

# Ensure we have a default file name if the user doesn't enter one
if not file_name:
    file_name = "qr_code"

# Validate that a URL was entered
if not url:
    print("A URL is required to generate a QR Code. Exiting.")
    exit(1)

# Create the QR Code instance with desired settings
qr = qrcode.QRCode(
    version=1,  # Controls the size (1 is smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each box in pixels
    border=4,     # Thickness of the border (in boxes)
)

qr.add_data(url)
qr.make(fit=True)

# Generate the image of the QR code
img = qr.make_image(fill_color="black", back_color="white")
output_filename = f"{file_name}.png"
img.save(output_filename)

print(f"QR Code generated and saved as {output_filename}")
