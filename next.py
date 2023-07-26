from sys import argv
from PIL import ImageTk, Image
import tkinter as tk
import json

data = open("country_data.json", "r")

jsondata = json.load(data)

population = jsondata[argv[1]]["population"]


def display_image(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(second_frame, image=photo)
    label.image = (
        photo  # Store the PhotoImage in a variable to avoid garbage collection
    )
    label.pack()


def display_population(population):
    label = tk.Label(second_frame, text=f"Population: {population}")
    label.pack()


def display_money(money):
    label = tk.Label(second_frame, text=f"Money: {money}")
    label.pack()


if __name__ == "__main__":
    country = argv[1] if len(argv) >= 2 else "default_country"

    root = tk.Tk()

    # Make the window fullscreen
    root.attributes("-fullscreen", True)

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # scrollbar
    my_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind(
        "<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    )

    second_frame = tk.Frame(my_canvas, width=1000, height=100)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    display_image("flags/" + country + ".png")
    display_population(f"{population:,}")
    display_money(f"{population:,}")

    root.mainloop()
