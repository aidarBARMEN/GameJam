import pygame
import sys
import math
import test
import importlib
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
score = 0

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Обруч с тремя сегментами')
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)


empty = pygame.image.load("Assets/empty.png")
fisherman = pygame.image.load("fisherman.png")
fisherman = pygame.transform.scale(fisherman, (300, 300))
backGround = pygame.image.load("Assets/backGround.jpg")
backGround = pygame.transform.scale(backGround, (WIDTH,HEIGHT))
shoe = pygame.image.load("Assets/shoe.png")
shoe = pygame.transform.scale(shoe, (50,50))

fish_images = [pygame.transform.scale(pygame.image.load(f"Assets/fishes/f{i}.png"), (50, 50)) for i in range(1, 5)]
fisherman_images = [pygame.transform.scale(pygame.image.load(f"Assets/fisherman/{i}.PNG"), (300, 300)) for i in range(1, 5)]

fishermanPos = (250, 150)
fishPos = (600, 0)

velocity = 2

isFishCatched = False


angle = 0
rotatingSpeed = 5

def draw_hoop(screen, x, y, radius, segments, angle):
    colors = [(0, 255, 0), (255, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 255)]
    greenArea = 0.02 * 360
    yellowArea = 0.03 * 360
    redArea = 0.06 * 360

    angle_step = 360 // segments
    segment1_end = angle_step * greenArea
    segment2_end = segment1_end + angle_step * yellowArea
    segment3_end = segment2_end + angle_step * redArea

    pygame.draw.arc(screen, colors[0], (x - radius, y - radius, 2 * radius, 2 * radius), math.radians(0), math.radians(segment1_end), 10)
    pygame.draw.arc(screen, colors[1], (x - radius, y - radius, 2 * radius, 2 * radius), math.radians(segment1_end), math.radians(segment2_end), 10)
    pygame.draw.arc(screen, colors[2], (x - radius, y - radius, 2 * radius, 2 * radius), math.radians(segment2_end), math.radians(segment3_end), 10)
    pygame.draw.arc(screen, colors[3], (x - radius, y - radius, 2 * radius, 2 * radius), math.radians(segment3_end), math.radians(360), 10)

    strip_radius = radius + 3
    strip_x = x + strip_radius * math.cos(math.radians(angle))
    strip_y = y - strip_radius * math.sin(math.radians(angle))
    pygame.draw.circle(screen, colors[4], (int(strip_x), int(strip_y)), 3)

    return segment1_end, angle, strip_x, strip_y

def catch_fish(currentAngle,fishPos, score):
    running = True
    frame = 0
    screen.blit(backGround,(0,0))
    draw_hoop(screen, 70, 100, 50, 360, currentAngle)
    font = pygame.font.SysFont(None, 36)
    
    
    score_text = font.render(f"Очки: {score}", True, (0, 255, 2))
    screen.blit(text, (10, 10))
    screen.blit(score_text, (700, 10))
    # Сохраняем текущее состояние экрана
    saved_screen = screen.copy()
    randFish = random.randint(0,len(fish_images)- 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(saved_screen, (0, 0))
        if zone == "идеальная":
            screen.blit(fish_images[randFish], fishPos)
        elif zone == "хорошая":
            screen.blit(fish_images[randFish], fishPos)
        elif zone == "плохая":
            screen.blit(shoe, fishPos)
        else:
            score -= 5
            if score < 0:
                score = 0


        # Отображение текущего кадра анимации
        current_frame = fisherman_images[frame]
        screen.blit(current_frame, fishermanPos)

        pygame.display.flip()

        clock.tick(5)  # Задержка между кадрами анимации

        frame += 1
        if frame >= len(fisherman_images):
            running = False


ticks = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(backGround,(0,0))

    
    ticks = clock.tick(30)

    segment1_end, angle, strip_x, strip_y = draw_hoop(screen, 70, 100, 50, 360, angle)
    zone = ""
    if 0 <= angle <= segment1_end:
        zone = "идеальная"
    elif segment1_end <= angle <= segment1_end + 0.02 * 360:
        zone = "хорошая"
    elif segment1_end + 0.03 * 360 <= angle <= segment1_end + 0.09 * 360:
        zone = "плохая"
    else:
        zone = "вне зоны"

    screen.blit(fisherman, fishermanPos)
    screen.blit

    text = font.render(f"Зона: {zone}", True, (255, 255, 255))
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    screen.blit(score_text, (700, 10))

    pygame.display.flip()
    angle += rotatingSpeed
    if angle >= 360:
        angle = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        catch_fish(angle,fishPos,score)
        rotatingSpeed += 0.5
        print(rotatingSpeed)
        if zone == "идеальная":
            score += 5
        elif zone == "хорошая":
            score += 3
        elif zone == "плохая":
            score += 1
        else:
            score -= 5
            if score < 0:
                score = 0