import tkinter as tk
import pygame
import random

class SimonGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simon Game")
        self.original_colors = {
            "Red": "red",
            "Blue": "blue",
            "Yellow": "yellow",
            "Green": "green"
        }

        self.original_sounds = {
            "Red": 'output.wav',
            "Blue": 'output1.wav',
            "Yellow": 'output2.wav',
            "Green": 'output3.wav',
        }

        self.sequence = []
        self.player_sequence = []
        self.round = 1
        self.game_over = False

        self.create_buttons()
        self.create_reset_button()
        self.next_round()

    def create_buttons(self):
        self.buttons = {}
        button_height = 4  # Set the button height
        button_width = 10  # Set the button width

        for color, color_code in self.original_colors.items():
            self.buttons[color] = tk.Button(self.root, text=color, bg="gray",
                                            command=lambda color=color: self.handle_button_click(color))
            self.buttons[color].config(height=button_height, width=button_width)
            self.buttons[color].grid(row=0, column=list(self.original_colors.keys()).index(color), padx=10, pady=10)

    def create_reset_button(self):
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=1, column=0, columnspan=len(self.original_colors), padx=10, pady=10)

    def next_round(self):
        self.sequence.append(random.choice(list(self.original_colors.keys())))
        self.update_title()
        self.play_sequence()

    def update_title(self):
        self.root.title(f"Simon Game - Round {self.round}")

    def play_sequence(self):
        self.root.after(1000, self.flash_colors, 0)

    def flash_colors(self, index):
        if index < len(self.sequence):
            color = self.sequence[index]
            self.toggle_color(color)
            self.root.after(1000, self.flash_colors, index + 1)
        else:
            self.player_sequence = []
            self.game_over = False

    def toggle_color(self, color):
        button = self.buttons[color]
        button.config(bg=self.original_colors[color])
        self.play_button_click_sound(self.original_sounds[color])
        self.root.after(500, lambda: button.config(bg="gray"))

    def play_button_click_sound(self, sound_file):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

    def handle_button_click(self, color):
        if not self.game_over:
            self.toggle_color(color)
            self.player_sequence.append(color)

            if self.player_sequence != self.sequence[:len(self.player_sequence)]:
                self.end_game()
            elif len(self.player_sequence) == len(self.sequence):
                self.round += 1
                self.update_title()
                self.root.after(1000, self.next_round)

    def end_game(self):
        self.root.title(f"Simon Game - Game Over (Round {self.round})")
        self.game_over = True
        self.sequence = []
        self.player_sequence = []

    def reset_game(self):
        self.sequence = []
        self.player_sequence = []
        self.round = 1
        self.update_title()
        self.game_over = False
        self.next_round()

if __name__ == "__main__":
    game = SimonGame()
    game.root.mainloop()
