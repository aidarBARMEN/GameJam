import pygame
from pygame.sprite import Group
import input
from player import Player 
from sprite import sprites, Sprite
from camera import create_screen

def load_scene(screen):
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    screen = create_screen(800, 600, "PP2")
    clear_color = (135,100,100)
    running = True
    movement_speed =2 

    background_image = pygame.image.load("images/kbtu.png").convert()
    background_image = pygame.transform.scale(background_image, (800,600))

    player_image = pygame.transform.scale(pygame.image.load("images/player.png"), (32, 64))
    player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    albert_image = pygame.transform.scale(pygame.image.load("npcs/albert.png"), (32, 64))
    albert_rect = albert_image.get_rect(center=(200, 300))

    aknur_image = pygame.transform.scale(pygame.image.load("npcs/aknur.png"), (32, 64))
    aknur_rect = aknur_image.get_rect(center=(740, 400))

    left_image = pygame.transform.scale(pygame.image.load("images/left.png"), (20, 20))
    left_rect = left_image.get_rect(center=(200 + albert_rect.width, 320))

    right_image = pygame.transform.scale(pygame.image.load("images/right.png"), (20, 20))
    right_rect = right_image.get_rect(center=(730 - aknur_rect.width, 420))

    text_box_image = pygame.transform.scale(pygame.image.load("images/text_box.png"),(500,170))
    text_box_rect = text_box_image.get_rect(center=(WIDTH // 2, 500))

    conversation_texts = [
        "How are you?",
        "Fine...",
        "What's your name?",
        "Arnur",
        "You're doing a good job, Arnor",
        "We're trying our best",
        "Do you want to meet some decent people?",
        "You'll earn good money, and see America",
        "Let's see"
    ]
    conversation_speakers = [
        "Albert",
        "Player",
        "Albert",
        "Player",
        "Albert",
        "Arnur",
        "Albert",
        "Albert",
        "Arnur"
    ]

    conversation_index = 0
    in_conversation = False

    conversation_texts_left = [
    "Hello there!",
    "Nice to see you!",
    "Lovely weather, isn't it?",
    "Have you seen any great sights around here?",
    "Sure, for instance arba..",
    "Yeah, Arbat!",
    "Tommorow, we'll have a great event there",
    "What are your plans for tommorow?",
    "In general, I am a super busy person..",
    "Great! you will run ALMATY MARAPHON",
    "Hm, but I have some plans...",
    "Take care, I will wait you at 9:00",
    "Damn! But I''be heathier:)"
    ]
#13
    conversation_speakers_left = [
        "Albert",
        "Albert",
        "Albert",
        "Albert",
        "Arnur",
        "Albert",
        "Albert",
        "Albert",
        "Arnur",
        "Albert",
        "Arnur",
        "Albert",
        "Arnur"
    ]
    #13
    conversation_index_left = 0
    in_conversation_left= False
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if in_conversation:
                    if conversation_index < len(conversation_texts) - 1:
                        conversation_index += 1
                    else:
                        in_conversation = False
                        conversation_index = 0
                if in_conversation_left:
                    if conversation_index_left < len(conversation_texts_left) - 1:
                        conversation_index_left += 1
                    else:
                        in_conversation_left = False
                        conversation_index_left = 0


        screen.blit(background_image, (0, 0))
        screen.blit(left_image, left_rect)
        screen.blit(right_image, right_rect)
        screen.blit(player_image, player_rect)
        screen.blit(albert_image, albert_rect)
        screen.blit(aknur_image, aknur_rect)

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            player_rect.y -= movement_speed
        if key[pygame.K_s]:
            player_rect.y += movement_speed
        if key[pygame.K_a]:
            player_rect.x -= movement_speed
        if key[pygame.K_d]:
            player_rect.x += movement_speed

        if player_rect.colliderect(albert_rect) or player_rect.colliderect(aknur_rect):
            if key[pygame.K_w]:
                player_rect.y += movement_speed
            if key[pygame.K_s]:
                player_rect.y -= movement_speed
            if key[pygame.K_a]:
                player_rect.x += movement_speed
            if key[pygame.K_d]:
                player_rect.x -= movement_speed

        if player_rect.colliderect(right_rect):
            in_conversation = True
            screen.blit(text_box_image, text_box_rect)
            font = pygame.font.SysFont(None, 32)
            font_speaker = pygame.font.SysFont("fonts/lion_king.ttf", 36)
            speaker_text = font_speaker.render(conversation_speakers[conversation_index], True, (255, 255, 255))
            text = font.render(conversation_texts[conversation_index], True, (255, 255, 255))
            screen.blit(text, (text_box_rect.centerx - text.get_width() // 2, text_box_rect.centery - text.get_height() // 2))
            screen.blit(speaker_text, (WIDTH // 2 - 230, 430))

        if player_rect.colliderect(left_rect):
            in_conversation_left = True
            screen.blit(text_box_image, text_box_rect)
            font = pygame.font.SysFont(None, 32)
            font_speaker = pygame.font.SysFont("fonts/lion_king.ttf", 36)
            speaker_text = font_speaker.render(conversation_speakers_left[conversation_index_left], True, (255, 255, 255))
            text = font.render(conversation_texts_left[conversation_index_left], True, (255, 255, 255))
            screen.blit(text, (text_box_rect.centerx - text.get_width() // 2, text_box_rect.centery - text.get_height() // 2))
            screen.blit(speaker_text, (WIDTH // 2 - 230, 430))

        for s in sprites:
            s.draw(screen)
        pygame.display.flip()

        pygame.time.delay(17)

    pygame.quit()