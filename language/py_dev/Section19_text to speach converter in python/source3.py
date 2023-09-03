"""
 code snippet that uses the Tkinter library in Python to create a simple GUI where the user can enter text or select a text file to convert it to audio using the gTTS library:
 
"""

import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import os

def convert_text_to_speech():
    text = text_entry.get("1.0", "end-1c")
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("mpg123 output.mp3")
    else:
        print("No text entered")

def convert_file_to_speech():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("mpg123 output.mp3")
    else:
        print("No file selected")

# Create the GUI
window = tk.Tk()
window.title("Text to Speech Converter")

# Text Entry
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Convert Text Button
convert_text_button = tk.Button(window, text="Convert Text", command=convert_text_to_speech)
convert_text_button.pack()

# Convert File Button
convert_file_button = tk.Button(window, text="Convert File", command=convert_file_to_speech)
convert_file_button.pack()

# Run the GUI main loop
window.mainloop()


"""
In this example, we create a simple GUI using Tkinter. The GUI has a text entry widget where the user can enter text, a "Convert Text" button to convert the entered text to audio, and a "Convert File" button to select a text file and convert its contents to audio.

The convert_text_to_speech function is called when the "Convert Text" button is clicked. It retrieves the text entered in the text entry widget using text_entry.get("1.0", "end-1c"). If there is text entered, it uses the gTTS library to generate an audio file, saves it as "output.mp3", and plays it using the os.system command.

The convert_file_to_speech function is called when the "Convert File" button is clicked. It opens a file dialog using filedialog.askopenfilename to allow the user to select a text file. If a file is selected, it reads its contents, uses gTTS to generate an audio file, saves it as "output.mp3", and plays it using the os.system command.

Please make sure you have the necessary dependencies installed (gtts, mpg123) before running this code.


"""