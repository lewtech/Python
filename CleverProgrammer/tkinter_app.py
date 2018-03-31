import tkinter as tk


window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text = "test")
alabel.grid(column=0, row =0)

button = tk.Button(text = "smash")
button.grid(column = 0)

window.mainloop()