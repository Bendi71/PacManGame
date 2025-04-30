import pygame
import os

class SoundManager:
    def __init__(self):
        """Initialize the sound manager with game sounds"""
        # Ensure mixer is initialized
        pygame.mixer.init()
        
        # Sound file paths (relative to the Pac man directory)
        sound_dir = os.path.join("..", "sounds")
        
        # Load sound effects
        self.eat_sound = pygame.mixer.Sound(os.path.join(sound_dir, "eat_sound.wav"))
        self.power_up = pygame.mixer.Sound(os.path.join(sound_dir, "power_up.wav"))
        self.game_over = pygame.mixer.Sound(os.path.join(sound_dir, "game_over.wav"))
        self.pacman_death = pygame.mixer.Sound(os.path.join(sound_dir, "pacman_death.wav"))
        self.eat_ghost = pygame.mixer.Sound(os.path.join(sound_dir, "pacman_eatghost.wav"))
        self.intro_music = pygame.mixer.Sound(os.path.join(sound_dir, "pacman_beginning.wav"))
        
        # Set default volumes
        self.eat_sound.set_volume(0.4)
        self.power_up.set_volume(0.6)
        self.game_over.set_volume(0.8)
        self.pacman_death.set_volume(0.7)
        self.eat_ghost.set_volume(0.6)
        self.intro_music.set_volume(0.5)
        
        # Flag to track if intro music is playing
        self.intro_playing = False
    
    def play_eat_sound(self):
        """Play sound for eating a regular pellet"""
        self.eat_sound.play()
    
    def play_power_up(self):
        """Play sound for eating a power pellet"""
        self.power_up.play()
    
    def play_game_over(self):
        """Play sound for game over"""
        self.game_over.play()
        
    def play_pacman_death(self):
        """Play sound for Pac-Man dying"""
        self.pacman_death.play()
        
    def play_eat_ghost(self):
        """Play sound for eating a ghost"""
        self.eat_ghost.play()
        
    def play_intro_music(self):
        """Play intro music in a loop until stopped"""
        if not self.intro_playing:
            # -1 means loop indefinitely
            self.intro_music.play(-1)
            self.intro_playing = True
            
    def stop_intro_music(self):
        """Stop the intro music"""
        if self.intro_playing:
            self.intro_music.stop()
            self.intro_playing = False