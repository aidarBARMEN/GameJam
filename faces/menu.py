import pygame
import sys
import main
import importlib

try:
    mainScene = importlib.import_module("main")
except:
    print("Hello world")
try:
    mainScene = importlib.import_module("fish")
except:
    print("Hello world")    

# Инициализация Pygame
pygame.init()

# Установка размеров окна
SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")
# Загрузка изображения заднего фона
background_image = pygame.image.load("images/backmenu.png").convert()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Шрифты
pixel_font = pygame.font.Font("fonts/PressStart2P.ttf", 20)  # Здесь указывается путь к файлу шрифта и его размер

font = pygame.font.Font(None, 36)
# Загрузка и воспроизведение музыки
pygame.mixer.music.load("music/piala.mp3")
pygame.mixer.music.play(-1)  # -1 означает, что музыка будет воспроизводиться в цикле


# Определение функции для рисования кнопок с текстурой и пиксельным шрифтом
def draw_button_texture(surface, texture_path, x, y, width, height, text, text_color):
    button_texture = pygame.image.load(texture_path)  # Загрузка текстурного изображенияe
    button_texture = pygame.transform.scale(button_texture, (width, height))  # Масштабирование текстуры до нужного размера
    surface.blit(button_texture, (x, y))  # Отображение текстуры на экране
    text_surface = pixel_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width/2, y + height/2))
    surface.blit(text_surface, text_rect)

# Основной цикл игры
def main_menu():
    while True:
        screen.blit(background_image, (0, 0))  # Нарисуйте задний фон

        
        # Рисуем кнопки
        draw_button_texture(screen, "images/texturebutton.png", 300, 200, 200, 50, "Start", BLACK)
        draw_button_texture(screen, "images/texturebutton.png", 300, 300, 200, 50, "Quit", BLACK)
        draw_button_texture(screen, "images/texturebutton.png", 300, 400, 200, 50, "Settings", BLACK)
        
        # Проверка событий
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 300 <= mouse_pos[0] <= 500 and 200 <= mouse_pos[1] <= 250:
                    if mainScene:
                        mainScene.load_scene(screen)
                elif 300 <= mouse_pos[0] <= 500 and 300 <= mouse_pos[1] <= 350:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()

# Запуск главного меню
main_menu()
