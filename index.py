import tkinter as tk
from tkinter import ttk
from os import system

country = ""

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()


def sel():
    global country
    country = ""
    country = var.get()
    print(country)


root.geometry("%dx%d" % (width, height))

root.title("DebtSim")

var = tk.StringVar()


def next():
    system("python3 next.py " + country)
    quit(0)


# Text
message = ttk.Label(root, text="Pick a country:")
message.pack(anchor=tk.W)

# Select
exit_button = ttk.Button(root, text="Select", command=next)

exit_button.pack(anchor=tk.W)

# Buttons
R1 = ttk.Radiobutton(root, text="Andorra", variable=var, value="Andorra", command=sel)
R1.pack(anchor=tk.W)

R2 = ttk.Radiobutton(
    root,
    text="United Arab Emirates",
    variable=var,
    value="United Arab Emirates",
    command=sel,
)
R2.pack(anchor=tk.W)

R3 = ttk.Radiobutton(
    root, text="Afghanistan", variable=var, value="Afghanistan", command=sel
)
R3.pack(anchor=tk.W)

R4 = ttk.Radiobutton(
    root,
    text="Antigua and Barbuda",
    variable=var,
    value="Antigua and Barbuda",
    command=sel,
)
R4.pack(anchor=tk.W)

root.mainloop()
