import tkinter as tk
import subprocess
import time
import pygame
import PIL


def run_splash_screen():
    # runs splash-screen.py script
    subprocess.run(["python", "c:\\Users\\bcrbl\\Comp-Sci code\\python\\AGC\\splash-screen.py"], check=True)

def mainmenu():
    # runs mainmenu.py script
    subprocess.run(["python", "c:\\Users\\bcrbl\\Comp-Sci code\\python\\AGC\\mainmenu.py"], check=True)
    
def run_game():
    subprocess.run(["python", "c:\\Users\\bcrbl\\Comp-Sci code\\python\\AGC\\game.py"], check=True)
    

def main():
    run_splash_screen()
    time.sleep(2)  # Optional delay between splash screen and main menu
    mainmenu()

if __name__ == "__main__":
    main()