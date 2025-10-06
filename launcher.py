import tkinter as tk
import subprocess
import time
import pygame
import PIL
import os


def run_splash_screen():
    # runs splash-screen.py script
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), "splash-screen.py")], check=True) # now can be ran on any pc

def mainmenu():
    # runs mainmenu.py script
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), "mainmenu.py")], check=True)
    
def run_game():
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), "game.py")], check=True)


def main():
    run_splash_screen()
    time.sleep(2)  # Optional delay between splash screen and main menu
    mainmenu()

if __name__ == "__main__":
    main()