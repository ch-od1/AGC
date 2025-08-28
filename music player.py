import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Try to load and play the music
try:
    pygame.mixer.music.load("C:/Users/bcrbl/Comp-Sci code/python/AGC/assets/01 - Test Your Fate.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Loops forever
    print("Pygame music is playing!")
except Exception as e:
    print(f"Error with Pygame: {e}")

# Keep the Pygame window running
pygame.time.wait(5000)  # Keep Pygame running for 5 seconds
pygame.quit()
