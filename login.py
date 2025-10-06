import tkinter as tk
from PIL import Image, ImageTk
import smtplib, ssl
import subprocess as sp




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

def get_username():
    return username_entry.get()


def get_password():
    return password_entry.get()


def login():
    username = username_entry.get()
    password = password_entry.get()
    validator()
    
    
def validator():
    # Placeholder for actual validation logic
    # Here you would typically check the username and password against a database or file
    if username_entry.get() == "user" and password_entry.get() == "pass":
        tk.messagebox.showinfo("Login Successful", "Welcome back!")
        root.destroy()
        sp.run(["python", "c:\\Users\\bcrbl\\Comp-Sci code\\python\\AGC\\game.py"], check=True)
    else:
        tk.messagebox.showerror("Login Failed", "Invalid username or password.")







root.mainloop()