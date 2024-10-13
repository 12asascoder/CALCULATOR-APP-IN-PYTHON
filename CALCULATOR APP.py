import tkinter as tk

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def clear():
    display.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)

button_layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in button_layout:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: display.insert(tk.END, t) if t != "=" else calculate())
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="C", padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=3)

root.mainloop()
