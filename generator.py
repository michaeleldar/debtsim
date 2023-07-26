import json

output = open("output.py", "w")
nations = open("country_data.json", "r")

data = json.load(nations)
x = 0

for country in data:
    y = x + 1
    output.write(
        f'R{y} = ttk.Radiobutton(second_frame, text="{country}", variable=var, value="{country}", command=sel)\n'
    )
    output.write(f"R{y}.pack(anchor=tk.W)\n")
    x = x + 1

"""
R1 = ttk.Radiobutton(root, text="Andorra", variable=var, value="Andorra", command=sel)
R1.pack(anchor=tk.W)
"""
