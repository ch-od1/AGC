import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# HERE IS THE WHERE THE MAIN MENU AND USER ACCOUNT CREATION GO
def main_menu():
    def on_create_account():
        messagebox.showinfo("AGC Main Menu", "Account creation selected.")
        root.destroy()
        subprocess.run(["python", os.path.join(os.path.dirname(__file__), "account-creation.py")], check=True)
        

    def on_login():
        messagebox.showinfo("AGC", "Login selected.")
        root.destroy()
        subprocess.run(["python", os.path.join(os.path.dirname(__file__), "login.py")], check=True)

    def on_exit():
        root.destroy()

    root = tk.Tk()
    root.title("AGC Launcher")

    tk.Label(root, text="AGC", font=("Arial", 50)).pack(pady=10)

    tk.Button(root, text="Create Account", command=on_create_account, width=20).pack(pady=5)
    tk.Button(root, text="Login", command=on_login, width=20).pack(pady=5)
    tk.Button(root, text="Exit", command=on_exit, width=20).pack(pady=5)
   
    # Centres the window on the screen for easier access
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.mainloop()

# Example usage
if __name__ == "__main__":
    main_menu()
