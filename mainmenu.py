import tkinter as tk
from tkinter import messagebox

# HERE IS THE WHERE THE MAIN MENU AND USER ACCOUNT CREATION GO
def main_menu():
    def on_create_account():
        messagebox.showinfo("AGC Main Menu", "Account creation selected.")

    def on_login():
        messagebox.showinfo("AGC Main Menu", "Login selected.")

    def on_exit():
        root.destroy()

    root = tk.Tk()
    root.title("AGC Launcher")

    tk.Label(root, text="AGC", font=("Arial", 50)).pack(pady=10)

    tk.Button(root, text="Create Account", command=on_create_account, width=20).pack(pady=5)
    tk.Button(root, text="Login", command=on_login, width=20).pack(pady=5)
    tk.Button(root, text="Exit", command=on_exit, width=20).pack(pady=5)

    root.mainloop()

# Example usage
if __name__ == "__main__":
    main_menu()
