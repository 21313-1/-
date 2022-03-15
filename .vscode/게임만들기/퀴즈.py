from random import randint, random
from webbrowser import BackgroundBrowser
from xml.dom.minidom import CharacterData
import pygame
pygame.init()

        
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기")

clook = pygame.time.Clock()

background = pygame.image.load(".vscode\게임만들기/resource/background.png")

character = pygame.image.load(".vscode/게임만들기/resource/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width /2)
character_y_pos = screen_height - character_height
character_speed = 0.6

enemy = pygame.image.load(".vscode\게임만들기/resource\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 0.3

to_x_right = 0
to_x_left = 0


running = True
while running:
    dt = clook.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x_left -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_right += character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_x_left = 0
            elif event.key == pygame.K_RIGHT:
                to_x_right = 0
    

    character_x_pos += (to_x_left + to_x_right) * dt

    #enemy 이동 처리
    enemy_y_pos += enemy_speed *dt
    if enemy_y_pos >= screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randint(0, screen_width - enemy_width)
        print(enemy_x_pos)

    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    #충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        running = False
    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()



pygame.quit