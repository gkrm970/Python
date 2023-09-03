import tkinter as tk

main_window = tk.Tk()
main_window.geometry("500x300")
entry = tk.Entry(main_window, bg="grey", fg="white", justify="right",
                 font="Ariel 16 bold", bd=4)
entry.pack()
main_window.mainloop()
