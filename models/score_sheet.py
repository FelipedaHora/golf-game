import pygame

class scoreSheet:
    def __init__(self, parr, win, winwidth, winheight):
        self.parList = parr
        self.par = sum(self.parList)
        self.holes = 9
        self.finalScore = None
        self.parScore = 0
        self.strokes = []
        self.win = win
        self.winwidth = winwidth
        self.winheight = winheight
        self.width = 400
        self.height = 510
        self.font = pygame.font.SysFont('comicsansms', 22)
        self.bigFont = pygame.font.SysFont('comicsansms', 30)

    def getScore(self):
        return sum(self.strokes) - sum(self.parList[:len(self.strokes)])

    def getPar(self):
        return self.par

    def getStrokes(self):
        return sum(self.strokes)

    def drawSheet(self, score=0):
        self.strokes.append(score)
        grey = (220, 220, 220)

        text = self.bigFont.render('Batidas: ' + str(sum(self.strokes)), 1, grey)
        self.win.blit(text, (800, 330))
        text = self.bigFont.render('Par: ' + str(self.par), 1, grey)
        self.win.blit(text, (240 - (text.get_width()/2), 300 - (text.get_height()/2)))
        text = self.bigFont.render('Pontos: ', 1, grey)
        self.win.blit(text, (800, 275))

        scorePar = sum(self.strokes) - sum(self.parList[:len(self.strokes)])
        if scorePar < 0:
            color = (0,166,0)
        elif scorePar > 0:
            color = (255,0,0)
        else:
            color = grey

        textt = self.bigFont.render(str(scorePar), 1, color)
        self.win.blit(textt, (805 + text.get_width(), 275))

        startx = self.winwidth/2 - self.width /2
        starty = self.winheight/2 - self.height/2
        pygame.draw.rect(self.win, grey, (startx, starty, self.width, self.height))

        # Set up grid
        for i in range(1,4):
            # Column Lines
            pygame.draw.line(self.win, (0,0,0), (startx + (i * (self.width/3)), starty), (startx + (i * (self.width/3)), starty + self.height), 2)
        for i in range(1, 11):
            # Rows
            if i == 1:  # Display all headers for rows
                blit = self.font.render('Buraco', 2, (0,0,0))
                self.win.blit(blit, (startx + 40, starty + 10))
                blit = self.font.render('Par', 2, (0,0,0))
                self.win.blit(blit, (startx + 184, starty + 10))
                blit = self.font.render('Batida', 2, (0,0,0))
                self.win.blit(blit, (startx + 295, starty + 10))
                blit = self.font.render('Aperte para continuar...', 1, (128,128,128))
                self.win.blit(blit, (384, 565))
            else:  # Populate rows accordingly
                blit = self.font.render(str(i - 1), 1, (128,128,128))
                self.win.blit(blit, (startx + 56, starty + 10 + ((i - 1) * (self.height/10))))

                blit = self.font.render(str(self.parList[i - 2]), 1, (128,128,128))
                self.win.blit(blit, (startx + 60 + 133, starty + 10 + ((i - 1) * (self.height/10))))
                try:  # Catch the index out of range error, display the stokes each level
                    if self.strokes[i - 2] < self.parList[i - 2]:
                        color = (0,166,0)
                    elif self.strokes[i - 2] > self.parList[i - 2]:
                        color = (255,0,0)
                    else:
                        color = (0,0,0)

                    blit = self.font.render(str(self.strokes[i - 2]), 1, color)
                    self.win.blit(blit, ((startx + 60 + 266, starty + 10 + ((i - 1) * (self.height/10)))))
                except:
                    blit = self.font.render('-', 1, (128,128,128))
                    self.win.blit(blit, (startx + 62 + 266, starty + 10 + ((i - 1) * (self.height/10))))

            # Draw row lines
            pygame.draw.line(self.win, (0,0,0), (startx, starty + (i * (self.height/10))), (startx + self.width, starty + (i * (self.height / 10))), 2)
