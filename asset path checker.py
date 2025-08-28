# DELETE WHEN FINISH PROGRAMMING.
# THIS IS USED TO MANUALLY FIND FILE IMAGES SO ITS EASIER



import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # hides the root window

file_path = filedialog.askopenfilename(title="Select your file")
print("Selected file path:", file_path)
