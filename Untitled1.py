#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import random
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Палач")
font_small = pygame.font.Font(None, 30)
font_large = pygame.font.Font(None, 60)
WORDS = ["Кошка", "Собака", "Машина", "Дом", "Человек", "Книга", "Карандаш", "Стул", "Стол", "Окно"]
MAX_ERRORS = 6
word_to_guess = random.choice(WORDS)
guessed_letters = []
wrong_guesses = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                letter = event.unicode.upper()
                if letter not in guessed_letters and letter not in wrong_guesses:
                    if letter in word_to_guess:
                        guessed_letters.append(letter)
                        if set(guessed_letters) == set(word_to_guess):
                            message = font_large.render("Вы выиграли!", True, BLACK)
                            running = False
                    else:
                        wrong_guesses.append(letter)
                        if len(wrong_guesses) == MAX_ERRORS:
                            message = font_large.render("Вы проиграли!", True, BLACK)
                            running = False
    screen.fill(WHITE)
    word_text = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            word_text += letter + " "
        else:
            word_text += "_ "
    word_surface = font_large.render(word_text, True, BLACK)
    screen.blit(word_surface, (WINDOW_SIZE[0] // 2 - word_surface.get_width() // 2, 100))
    wrong_guesses_text = "Неправильные догадки: " + " ".join(wrong_guesses)
    wrong_guesses_surface = font_small.render(wrong_guesses_text, True, BLACK)
    screen.blit(wrong_guesses_surface, (10, 10))
    pygame.draw.line(screen, BLACK, (WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] - 50), (WINDOW_SIZE[0] // 2 + 100, WINDOW_SIZE[1] - 50), 5)
    if len(wrong_guesses) >= 1:
        pygame.draw.circle(screen, BLACK, (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 200), 20, 3)
    if len(wrong_guesses) >= 2:
        pygame.draw.line(screen, BLACK, (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 100), (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 180), 3)
    if len(wrong_guesses) >= 3:
        pygame.draw.line(screen, BLACK, (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 100), (WINDOW_SIZE[0] // 2 - 30, WINDOW_SIZE[1] - 50), 3)
    if len(wrong_guesses) >= 4:
        pygame.draw.line(screen, BLACK, (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 100), (WINDOW_SIZE[0] // 2 + 30, WINDOW_SIZE[1] - 50), 3)
    if len(wrong_guesses) >= 5:
        pygame.draw.line(screen, BLACK, (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 170), (WINDOW_SIZE[0] // 2 - 50, WINDOW_SIZE[1] - 150), 3)
    if len(wrong_guesses) >= 6:
        pygame.draw.line(screen, BLACK, (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 170), (WINDOW_SIZE[0] // 2 - 50, WINDOW_SIZE[1] + 150), 3)
    while(True):
        i = 1
    if not running:
        screen.blit(message, (WINDOW_SIZE[0] // 2 - message.get_width() // 2, 200))
    pygame.display.flip()
pygame.quit()


# In[ ]:




