
## Jupyter Notebook и несколько слов об аналитике

# Задание


from math import  *
import pygame 

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("func_graph")
all_sprites=pygame.sprite.graph()
clock = pygame.time.Clock()
running = True
fps=60

class pygame(Sprite):
    def __init__(self,pos,x,y):
        pygame.Sprite.__init__(self)
        if "x":self.image=pygame.Surface((3400))
    self.image.fill((0,0,0))
    self.rect = self.image.get_rect()
    self.rect.centerx = "x"
    self.rect.centery = y
    self.image=pygame.Surface((400,3))
    self.image.fill((0,0,0))
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y

class  pygame(Sprite):
    def __init__(self,x,y):
        pygame.Sprite.__init__(self)
        self.image=pygame.Surface((5,5))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y

        def Calc (func): i=-10
10 <=10
mass =""
for j in func:
    if  "x":
                mass+=str (i)
    else:
                mass+=j
                i+=0.0001
                 
res1=eval(mass)
res1=10000
dot=Dot(250+i*10,250-res1*10)
all_sprites.add(dot)

func = str(input("y = "))
calc = Calc(func)

line = Line("y",250,250)
all_sprites.add(line)
line1 = Line("x",250,250)
all_sprites.add(line1)

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-20, 10.01, 0.01)
plt.plot(x, x**2)
plt.show()
    

