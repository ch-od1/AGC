import tkinter as tk

root = tk.Tk()
root.title("Test Status")

label = tk.Label(root, text="Test passed", font=("Arial", 16))
label.pack(padx=20, pady=20)

root.mainloop()