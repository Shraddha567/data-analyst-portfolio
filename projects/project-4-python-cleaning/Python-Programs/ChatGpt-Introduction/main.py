import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)

# Display
entry = tk.Entry(
    root,
    font=("Arial", 20),
    borderwidth=5,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def button_click(value):
    entry.insert(tk.END, value)

def clear_display(event=None):
    entry.delete(0, tk.END)

def backspace(event=None):
    entry.delete(len(entry.get()) - 1, tk.END)

def calculate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
]

frame = tk.Frame(root)
frame.pack()

for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=6, height=2,
                        font=("Arial", 14), command=calculate)
    else:
        btn = tk.Button(frame, text=text, width=6, height=2,
                        font=("Arial", 14),
                        command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 14),
    height=2,
    command=clear_display
).pack(fill=tk.BOTH, padx=10, pady=5)

# 🔑 Keyboard bindings
root.bind("<Return>", calculate)     # Enter
root.bind("<Escape>", clear_display) # Esc
root.bind("<BackSpace>", backspace)

# Allow typing numbers/operators
def key_input(event):
    if event.char in "0123456789+-*/.":
        entry.insert(tk.END, event.char)

root.bind("<Key>", key_input)

root.mainloop()
