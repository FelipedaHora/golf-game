import pygame
import os
import tkinter as tk
from tkinter import messagebox
import sys

pygame.init()

win = pygame.display.set_mode((1080, 600))
title = pygame.image.load(os.path.join('img', 'title.png'))
back = pygame.image.load(os.path.join('img', 'back.png'))
course = pygame.image.load(os.path.join('img', 'course1.png'))
course1 = pygame.transform.scale(course, (200, 200))

font = pygame.font.SysFont('comicsansms', 24)

buttons = [[1080/2 - course1.get_width()/2, 260, course1.get_width(), course1.get_height(), 'Grassy Land']]
ballObjects = []
surfaces = []

def getBest():
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split()
        if l[0] == 'score':
            file.close()
            return l[1].strip()
    return 0
    file.close()

def getCoins():
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split()
        if l[0] == 'coins':
            file.close()
            return l[1].strip()

def getBallColor():
    global ballObjects
    for balls in ballObjects:
        if balls.equipped == True:
            return balls.color
    return None

def mainScreen(hover=False):
    global shopButton
    surf = pygame.Surface((1080, 600))
    w = title.get_width()
    h = title.get_height()
    surf.blit(back, (0,0))
    surf.blit(title, ((1080/2 - (w/2)), 50))
    if hover == True:
        text = font.render('', 1,(0, 0, 0))
    else:
        text = font.render('', 1, (51, 51, 153))
    surf.blit(text, (960, 12))
    shopButton = text.get_rect()
    shopButton[0] = 960
    shopButton[1] = 12
    # For course Button
    i = buttons[0]
    surf.blit(course1, (i[0], i[1]))
    text = font.render(i[4], 1, (51,51,153))
    surf.blit(text, (i[0] + ((i[3] - text.get_width())/2), i[1] + i[3] + 10))
    text = font.render('Best: ' + getBest(), 1, (51, 51, 153))
    surf.blit(text, (i[0] + ((i[3] - text.get_width())/2), i[1] + i[3] + 40))
    text = font.render('Coins: ' + getCoins(), 1, (51,51,153))
    surf.blit(text, (10, 10))
    
    win.blit(surf, (0,0))
    pygame.display.update()

def mouseOver(larger=False):
    global course1
    if larger:
        buttons[0][0] = 415
        buttons[0][1] = 220
        buttons[0][2] = 250
        buttons[0][3] = 250
        course1 = pygame.transform.scale(course, (250, 250))
    else:
        buttons[0][1] = 240
        buttons[0][0] = 440
        buttons[0][2] = 200
        buttons[0][3] = 200
        course1 = pygame.transform.scale(course, (200, 200))
    mainScreen()

def click(pos):
    for i in buttons:
        if pos[0] > i[0] and pos[0] < i[0] + i[2]:
            if pos[1] > i[1] and pos[1] < i[1] + i[3]:
                return i[4]
                break
    return None
