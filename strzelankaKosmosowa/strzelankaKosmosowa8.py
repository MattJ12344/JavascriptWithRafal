import math
import random

import pygame
from pygame import mixer, Surface

pygame.init()

ekran: Surface = pygame.display.set_mode((800, 600))

tlo = pygame.image.load('background.png')

mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.display.set_caption('Sttzrlanka Kosmosowa')

ikona: Surface = pygame.image.load('ufo.png')

pygame.display.set_icon(ikona)

wygladGracza: Surface  = pygame.image.load('player.png')

graczX: int = 370
graczY: int = 480
graczXZmianaMiejsca: int = 0

wygladPrzeciwnika: list[int] = []
przeciwnikX: list[int] = []
przeciwnikY: list[int] = []
przeciwnikXZmianaMiejsca: list[int] = []
przeciwnikYZmianaMiejsca: list[int] = []
liczbaPrzeciwnikow: int = 6

for i in range(liczbaPrzeciwnikow):
    wygladPrzeciwnika.append(pygame.image.load('enemy.png'))
    przeciwnikX.append(random.randint(0, 736))
    przeciwnikY.append(random.randint(50, 150))
    przeciwnikXZmianaMiejsca.append(4)
    przeciwnikYZmianaMiejsca.append(40)


wygladNaboju = pygame.image.load('bullet.png')
nabojX: int = 0
nabojY: int = 480
nabojXZmianaMiejsca: int = 0
nabojYZmianaMiejsca: int = 10
stanNaboju: str = "ready"

iloscPunktow: int = 0

czcionka = pygame.font.Font("freesansbold.ttf", 32)

textX: int = 10
textY: int = 10

gameOver: Surface = pygame.font.Font("freesansbold.ttf", 64)

def pokazPunkty(x, y):
    punkty = czcionka.render("Punkty : " + str(iloscPunktow), True, (255, 255, 255))
    ekran.blit(punkty, (x, y))

def  napisGameOver():
    nadTekstem = gameOver.render("GAME OVER", True, (255, 255, 255))
    ekran.blit(nadTekstem, (200, 250))

def gracz(x, y):
    ekran.blit(wygladGracza, (x, y))

def przeciwnik(x, y, i):
    ekran.blit(wygladPrzeciwnika[i], (x, y))

def atakujepociskiem(x, y):
    global stanNaboju
    stanNaboju = "fire"
    ekran.blit(wygladNaboju, (x + 16, y + 10))

def czyJestKolizja(przeciwnikX, przeciwnikY, nabojX, nabojY):
    dystans = math.sqrt(math.pow(przeciwnikX - nabojX, 2) + (math.pow(przeciwnikY - nabojY, 2)))

    if dystans < 27:
        return True
    else:
        return False


uciekanie = True

while uciekanie:
    ekran.fill((0, 0, 0))

    ekran.blit(tlo, (0, 0))

    for wydarzenie in pygame.event.get():
        if wydarzenie.type == pygame.QUIT:
            running = False

        if wydarzenie.type == pygame.KEYDOWN:
            if wydarzenie.key == pygame.K_LEFT:
                playerX_change = -5
            if wydarzenie.key == pygame.K_RIGHT:
                playerX_change = 5
            if wydarzenie.key == pygame.K_SPACE:
                if stanNaboju is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()

                    nabojX = graczX
                    atakujepociskiem(nabojX, nabojY)

        if wydarzenie.type == pygame.KEYUP:
            if wydarzenie.key == pygame.K_LEFT or wydarzenie.key == pygame.K_RIGHT:
                playerX_change = 0


    graczX += graczXZmianaMiejsca

    if graczX <= 0:
        graczX = 0
    elif graczX >= 736:
        graczX = 736


    for i in range(liczbaPrzeciwnikow):

        if przeciwnikY[i] > 440:
            for j in range(liczbaPrzeciwnikow):
                przeciwnikY[j] = 2000

            napisGameOver()
            break

        przeciwnikX[i] += przeciwnikXZmianaMiejsca[i]
        if przeciwnikX[i] <= 0:
            przeciwnikXZmianaMiejsca[i] = 4
            przeciwnikY[i] += przeciwnikYZmianaMiejsca[i]
        elif przeciwnikX[i] >= 736:
            przeciwnikXZmianaMiejsca[i] = -4
            przeciwnikY[i] += przeciwnikYZmianaMiejsca[i]

        kolizja = czyJestKolizja(przeciwnikX[i], przeciwnikY[i], nabojX, nabojY)

        if kolizja:
            dzwiekEksplozji = mixer.Sound("explosion.wav")
            dzwiekEksplozji.play()
            nabojY = 480
            stanNaboju = "ready"
            iloscPunktow += 1
            przeciwnikX[i] = random.randint(0, 736)
            przeciwnikY[i] = random.randint(50, 150)

        przeciwnik(przeciwnikX[i], przeciwnikY[i], i)

    if nabojY <= 0:
        nabojY = 480
        stanNaboju = "ready"

    if stanNaboju is "fire":
        atakujepociskiem(nabojX, nabojY)
        nabojY -= nabojYZmianaMiejsca


    gracz(graczX, graczY)
    pokazPunkty(textX, textY)
    pygame.display.update()