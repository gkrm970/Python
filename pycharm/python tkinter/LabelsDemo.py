import tkinter as tk

main_window = tk.Tk()
label = tk.Label(main_window, text="Hello Python", bg="grey", fg="white",
                 padx=100, pady=200, font="comicsansms 30 bold", relief="sunken")
# flat, groove, raised, ridge, solid, sunken
label.pack()

# adding photo to our interface
photo = tk.PhotoImage(file="img.png")
label1 = tk.Label(image=photo)
label1.pack()

main_window.mainloop()
