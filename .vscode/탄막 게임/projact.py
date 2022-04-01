from turtle import back
from xml.dom.minidom import CharacterData
import pygame
import ctypes

pygame.init()

u32 = ctypes.windll.user32
resolution = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
screen = pygame.display.set_mode((resolution))
pygame.display.set_caption("projact")

clook = pygame.time.Clock()

class Unit:
    def __init__(self):
        self.img = 0
    def unit(self, image):
        self.img = pygame.image.load(image)
        return self.img
    def middle_pos(self, x_pos, y_pos):
        self.size = self.img.get_rect().size
        self.x_pos = x_pos - (self.size[0] / 2)
        self.y_pos = y_pos - (self.size[1] / 2)
        return self.x_pos, self.y_pos


background = Unit()
background.unit(".vscode\탄막 게임\배경.png")

character = Unit()
character.unit(".vscode/탄막 게임/주인공.png")
character.middle_pos(resolution[0] / 2, resolution[1] / 2)
print(resolution)
# print(character.y_pos)

to_x_l = 0
to_x_r = 0
to_y = 0
character_speed = 0.6

running = True
while running:
    dt = clook.tick(150)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                to_x_l -= character_speed
            if event.key == pygame.K_d:
                to_x_r += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                to_x_l = 0
            if event.key == pygame.K_d:
                to_x_r = 0

    character.x_pos += (to_x_l + to_x_r) * dt
    screen.blit(background.img, (0, 0))
    screen.blit(character.img, (character.x_pos, character.y_pos))
    pygame.display.update()
    
    

pygame.quit