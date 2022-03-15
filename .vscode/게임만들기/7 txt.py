from cProfile import run
from mailbox import NotEmptyError
from threading import Timer
import pygame

pygame.init()

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640#세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#FPS
clook = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load(".vscode/게임만들기/resource/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load(".vscode/게임만들기/resource/character.png")
character_size = character.get_rect().size #캐릭터의 크기를 구해옴
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.6

#적(enemy) 캐릭터
enemy = pygame.image.load(".vscode\게임만들기/resource\enemy.png")
enemy_size = enemy.get_rect().size #캐릭터의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로 크기
enemy_height = enemy_size[1] #캐릭터 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로 절반 크기에 해당하는 곳에 위치(가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)


#타이머
game_font = pygame.font.Font(None, 40)
total_time = 10
strat_ticks = pygame.time.get_ticks()

#이벤트 루프
running = True
while running:
    dt = clook.tick(150) #게임화면의 초당 프레임 수를 설정
    
    #print("fps" + str(int(clook.get_fps())))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y +=character_speed

        if event.type == pygame.KEYUP: #방향키를 떄면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
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
        print("충돌했어요")
        running = False

    
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))#배경그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #타이머 넣기
    elapsed_time = (pygame.time.get_ticks() - strat_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    if total_time - elapsed_time < 0:
        print("타임아웃")
        running = False

    pygame.display.update()#게임화면을 다시 그리기!

#pygame 종료
pygame.time.delay(2000) #2초 대기   
pygame.quit