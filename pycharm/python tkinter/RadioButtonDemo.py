import tkinter as tk


def click_now():
    print("Radiobutton clicked : ", var.get())


main_window = tk.Tk()
main_window.title("Radiobutton demo")
var = tk.IntVar()
radio_button_1 = tk.Radiobutton(main_window, text="Red", command=click_now,
                                variable=var, value=1)
radio_button_1.pack()

radio_button_2 = tk.Radiobutton(main_window, text="Yellow", command=click_now,
                                variable=var, value=2)
radio_button_2.pack()

radio_button_3 = tk.Radiobutton(main_window, text="Green",
                                command=click_now, variable=var, value=3)
radio_button_3.pack()

main_window.mainloop()
