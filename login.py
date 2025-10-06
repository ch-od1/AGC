import tkinter as tk
from PIL import Image, ImageTk
import smtplib, ssl
import subprocess as sp
import os
# notes - remember to call subprocesses as sp in this file!!

root = tk.Tk()
root.title("Login Screen")

# title screen
title_frame = tk.Frame(root)
title_frame.pack(pady=10)
title_label = tk.Label(title_frame, text="AGC Login - Existing User", font=("Arial", 25))
title_label.pack()
# user inputs their user and password
form_frame = tk.Frame(root)
form_frame.pack(pady=20)

username_label = tk.Label(form_frame, text="Username:", font=("Arial", 14))
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(form_frame, font=("Arial", 14))
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(form_frame, text="Password:", font=("Arial", 14))
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(form_frame, font=("Arial", 14), show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)


def return_to_main_menu():
    root.destroy()
    sp.run(["python", os.path.join(os.path.dirname(__file__), "mainmenu.py")], check=True)

return_button = tk.Button(root, text="Return to Main Menu", font=("Arial", 14), command=return_to_main_menu)
return_button.pack(pady=10)



root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")








root.mainloop()