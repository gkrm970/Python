generates a QR code using pyqrcode, Tkinter, and PIL:

import pyqrcode
from PIL import ImageTk
import tkinter as tk

def generate_qr_code():
    # Get the text input from the user
    text = entry.get()

    # Generate the QR code
    qr_code = pyqrcode.create(text)

    # Save the QR code as an image file
    qr_code.png("qr_code.png", scale=10)

    # Open the QR code image using PIL
    image = ImageTk.PhotoImage(file="qr_code.png")

    # Display the QR code image in a Tkinter window
    window = tk.Toplevel(root)
    label = tk.Label(window, image=image)
    label.pack()

# Create the main Tkinter window
root = tk.Tk()

# Set the window title
root.title("QR Code Generator")

# Create a label and an entry for text input
label = tk.Label(root, text="Enter text:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to generate the QR code
button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
button.pack()

# Start the Tkinter event loop
root.mainloop()
