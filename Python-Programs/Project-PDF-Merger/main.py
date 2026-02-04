# pypdf is a Python library to read, extract, split, merge, and manipulate PDF files. Short, practical explanation 👇
'''Works with text-based PDFs (not scanned images)
Successor of older PyPDF2
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
import os

# Main window
root = tk.Tk()
root.title("PDF Merger")
root.geometry("400x250")
root.resizable(False, False)

selected_files = []

# Select PDFs
def select_pdfs():
    global selected_files
    selected_files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if selected_files:
        status_label.config(
            text=f"{len(selected_files)} PDF(s) selected",
            fg="green"
        )

# Merge PDFs
def merge_pdfs():
    if not selected_files:
        messagebox.showerror("Error", "No PDF files selected")
        return

    try:
        merger = PdfWriter()

        for pdf in selected_files:
            merger.append(pdf)

        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save merged PDF as"
        )

        if output_path:
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", "PDFs merged successfully ✅")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# UI Elements
tk.Label(
    root,
    text="PDF Merger Tool",
    font=("Arial", 16, "bold")
).pack(pady=15)

tk.Button(
    root,
    text="Select PDF Files",
    width=20,
    command=select_pdfs
).pack(pady=10)

tk.Button(
    root,
    text="Merge PDFs",
    width=20,
    command=merge_pdfs
).pack(pady=10)

status_label = tk.Label(root, text="No files selected", fg="red")
status_label.pack(pady=10)

root.mainloop() #run the GUI
'''
It is used to run GUI and root.mainloop means elements are running in your GUI and loop or Tkinter handles it

root.mainloop() keeps the GUI running, and Tkinter handles all user actions like clicks and typing.
'''