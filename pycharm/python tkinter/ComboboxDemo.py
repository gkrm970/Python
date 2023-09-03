import tkinter as tk
import tkinter.ttk as ttk


def on_click(a):
    print(combo_box1.get())


main_window = tk.Tk()
main_window.geometry("250x250")
combo_box1 = ttk.Combobox(main_window)
combo_box1['values'] = [1, 2, 3]
combo_box1.current(1)
combo_box1.bind("<<ComboboxSelected>>", on_click)
combo_box1.pack()

main_window.mainloop()
