import tkinter as tk
from tkinter import filedialog

def get_pdf_path_via_dialog() -> str:
    root = tk.Tk()
    root.withdraw()  # Hide Tkinter root window
    file_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF files", "*.pdf")])
    root.destroy()
    if not file_path:
        raise RuntimeError("No file selected")
    return file_path
