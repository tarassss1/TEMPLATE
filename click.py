import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Створення вікна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse Click Example")

# Основний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 - ліва кнопка мишки
                print("Left mouse button clicked at", event.pos)

    # Очищення екрану
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
