# import pygame
# import sys

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Обруч с тремя сегментами')
# clock = pygame.time.Clock()

# player_image = pygame.transform.scale(pygame.image.load("fisherman.png"), (300, 300))
# player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# other_image = pygame.transform.scale(pygame.image.load("fish.png"), (50, 50))
# other_rect = other_image.get_rect(center=(100, 100))

# movement_speed = 5

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill((0, 0, 0))
    
#     screen.blit(player_image, player_rect)
#     screen.blit(other_image, other_rect)

#     key = pygame.key.get_pressed()
#     if key[pygame.K_w]:
#         player_rect.y -= movement_speed
#     if key[pygame.K_s]:
#         player_rect.y += movement_speed
#     if key[pygame.K_a]:
#         player_rect.x -= movement_speed
#     if key[pygame.K_d]:
#         player_rect.x += movement_speed

#     # Проверка столкновения
#     if player_rect.colliderect(other_rect):
#         # Возвращаем игрока на его предыдущую позицию
#         if key[pygame.K_w]:
#             player_rect.y += movement_speed
#         if key[pygame.K_s]:
#             player_rect.y -= movement_speed
#         if key[pygame.K_a]:
#             player_rect.x += movement_speed
#         if key[pygame.K_d]:
#             player_rect.x -= movement_speed

#     pygame.display.flip()
#     clock.tick(60)
