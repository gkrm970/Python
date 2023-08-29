GUI application using the Tkinter library to compress and decompress files:

import tkinter as tk
import tkinter.filedialog as filedialog
import zlib

def compress_file():
    input_file = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if not input_file:
        return
    output_file = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Compressed Files", "*.bin")])
    if not output_file:
        return
    
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            compressed_data = zlib.compress(f_in.read())
            f_out.write(compressed_data)
    
    result_label.config(text=f'{input_file} compressed and saved as {output_file}')

def decompress_file():
    input_file = filedialog.askopenfilename(filetypes=[("Compressed Files", "*.bin")])
    if not input_file:
        return
    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not output_file:
        return
    
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            decompressed_data = zlib.decompress(f_in.read())
            f_out.write(decompressed_data)
    
    result_label.config(text=f'{input_file} decompressed and saved as {output_file}')

# Create the main window
window = tk.Tk()
window.title("File Compression")

# Create the compress button
compress_button = tk.Button(window, text="Compress", command=compress_file)
compress_button.pack(pady=10)

# Create the decompress button
decompress_button = tk.Button(window, text="Decompress", command=decompress_file)
decompress_button.pack(pady=10)

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the main window loop
window.mainloop()



"""
This code creates a simple GUI with two buttons: "Compress" and "Decompress". When the "Compress" button is clicked, it prompts the user to select an input file to compress and choose a location to save the compressed file. Similarly, the "Decompress" button prompts the user to select a compressed file and choose a location to save the decompressed file. The result label displays the status of the compression or decompression process.

Make sure to run this code using a Python environment that has Tkinter installed.
"""

compressing file from local directory.