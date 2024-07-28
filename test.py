# імпорт бібліотеки pygame
import pygame

pygame.init()

# створення головного вікна
window = pygame.display.set_mode((500, 500))

# кольори
white = (255, 255, 255)
black = (0, 0, 0)

# завантаження зображення фону та гравця
background = pygame.image.load('background.jfif')
player = pygame.image.load('bird.png')
bg_width, bg_height = background.get_size()

# початкова позиція фону та гравця
bg_x = 0
bg_y = 0
player_x = 250
player_y = 250

# розмір вікна
win_width, win_height = window.get_size()

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # отримання стану клавіш
    keys = pygame.key.get_pressed()
    
    # переміщення фону
    if keys[pygame.K_LEFT]:
        bg_x += 5
    if keys[pygame.K_RIGHT]:
        bg_x -= 5
    if keys[pygame.K_UP]:
        bg_y += 5
    if keys[pygame.K_DOWN]:
        bg_y -= 5
    
    # обмеження руху фону
    if bg_x > 0:
        bg_x = 0
    if bg_y > 0:
        bg_y = 0
    if bg_x < -bg_width + win_width:
        bg_x = -bg_width + win_width
    if bg_y < -bg_height + win_height:
        bg_y = -bg_height + win_height

    # заповнення вікна фоном
    window.fill(white)
    window.blit(background, (bg_x, bg_y))

    # відображення гравця
    window.blit(player, (player_x, player_y))

    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit()
