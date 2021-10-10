import pygame
import random
import math

# initializing the module
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))

# setting on screen
pygame.display.set_caption("GAME")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')
# player
player = pygame.image.load('ship.png')
playerx = 390
playery = 480
playerc = 0

enemy = []
enemyx = []
enemyy = []
enemyc = []
enemycy = []
enemydirec = []
number_enemies = 5

for i in range(number_enemies):
    enemy.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, 768))
    enemyy.append(random.randint(0, 200))
    enemyc.append(1)
    enemycy.append(1)
    enemydirec.append('right')
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


bullet = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletcy = 1
bulletstate = 'stop'

over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def playerp(x, y):
    screen.blit(player, (x, y))


def enemyp(x, y, i):
    screen.blit(enemy[i], (x, y))


def bullet_fire(x, y):
    global bulletstate
    bulletstate = 'fire'
    screen.blit(bullet, (x + 5, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    screen.fill((36, 37, 38))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerc = 5
            if event.key == pygame.K_LEFT:
                playerc = -5
            if event.key == pygame.K_SPACE:
                if bulletstate == 'stop':
                    bulletx = playerx
                    bullet_fire(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerc = 0
    playerx += playerc
    if playerx < 0:
        playerx = 0
    if playerx >= 768:
        playerx = 768
    for i in range(number_enemies):
        if enemyy[i] >= 400:
            game_over_text()
            break
        if enemydirec[i] == 'right':
            enemyx[i] += enemyc[i]
        if enemydirec[i] == 'left':
            enemyx[i] -= enemyc[i]

        if enemyx[i] < 0:
            enemyx[i] = 0
            enemydirec[i] = 'right'

        if enemyx[i] >= 768:
            enemyx[i] = 768
            enemydirec[i] = 'left'
        enemyy[i] += enemycy[i]
        if bullety <= 0:
            bullety = 480
            bulletstate = 'stop'
        if bulletstate == "fire":
            bullety -= bulletcy
            bullet_fire(bulletx, bullety)
        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bulletstate = 'stop'
            bullety = 480
            enemyx[i] = random.randint(0, 768)
            enemyy[i] = random.randint(0, 200)
            score_value += 1

        enemyp(enemyx[i], enemyy[i], i)
    show_score(0, 0)
    playerp(playerx, playery)
    pygame.display.update()
