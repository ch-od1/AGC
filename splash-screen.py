import tkinter as tk  
from PIL import Image, ImageTk
import time
import pygame

fade_in_animation = 1300   # in milliseconds
fade_out_animation = 3500  
display_length = 1300   
splash_screen_location = r"C:/Users/bcrbl/Comp-Sci code/python/AGC/assets/splash.png"
splash_music_location = r"C:/Users/bcrbl/Comp-Sci code/python/AGC/assets/splashmusic.wav"


pygame.mixer.init()
pygame.mixer.music.load(splash_music_location)
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play()

def fade_in_anim(window, step=0.005):
    alpha = window.attributes('-alpha')
    if alpha < 1.0:
        alpha = min(alpha + step, 1.0)
        window.attributes('-alpha', alpha)
        window.after(int(fade_in_animation * step), fade_in_anim, window, step)
    else:
        window.after(fade_out_animation, fade_out_anim, window, step)

def fade_out_anim(window, step=0.005):
    alpha = window.attributes('-alpha')
    if alpha > 0.0:
        alpha = max(alpha - step, 0.0)
        window.attributes('-alpha', alpha)
        window.after(int(fade_out_animation * step), fade_out_anim, window, step)
    else:
        window.destroy()

def splash():
    root = tk.Tk()
    root.overrideredirect(True)  # makes the window borderless so user cannot close it 
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.0)  # starts transparant 

    img = Image.open(splash_screen_location)
    photo = ImageTk.PhotoImage(img)
    w, h = img.size

    screen_w = root.winfo_screenwidth()  # this snippet here checks the screen size
    screen_h = root.winfo_screenheight()
    x = (screen_w // 2) - (w // 2)
    y = (screen_h // 2) - (h // 2)    # this snippet here puts the splash screen on the centre of the screen
    root.geometry(f"{w}x{h}+{x}+{y}") # this sets the window size and position using an f string due to it being efficient and they are variables

    label = tk.Label(root, image=photo, borderwidth=0)
    label.image = photo
    label.pack()

    fade_in_anim(root)

    root.mainloop()

splash()


