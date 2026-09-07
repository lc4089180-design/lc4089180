#Use ChatGPT or GitHub Copilot to suggest a third-party Python package that can generate QR codes for payment links, then install the suggested package with pip and write a script called generate_qr.py that creates a QR code for a sample UPI payment link.<br><br><em><strong>Hint:</strong> Ask the AI tool for both the package name and a basic code example.</em>
#task5.py
import qrcode

upi_link = "upi://pay?pa=demo@upi&pn=Kavita&am=100&cu=INR"

qr = qrcode.make(upi_link)

qr.save("upi_payment_qr.png")

print("QR code generated successfully!")
print("Saved as: upi_payment_qr.png")