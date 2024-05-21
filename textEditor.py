import tkinter as tk
from tkinter import filedialog


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            text = text_area.get("1.0", tk.END)
            file.write(text)


root = tk.Tk()
root.title("Text Editor")

text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=True)

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

root.mainloop()
