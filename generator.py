output = open("output.py", "w")
nations = open("nations.txt", "r").read().split("\n")

for x in range(0, 250):
    y = x + 1
    output.write(
        f'R{y} = ttk.Radiobutton(second_frame, text="{nations[x]}", variable=var, value="{nations[x]}", command=sel)\n'
    )
    output.write(f"R{y}.pack(anchor=tk.W)\n")

"""
R1 = ttk.Radiobutton(root, text="Andorra", variable=var, value="Andorra", command=sel)
R1.pack(anchor=tk.W)
"""
