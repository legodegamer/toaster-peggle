import pygame, sys, math, time, random, pygame.midi
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((96*7, 96*7))
clock = pygame.time.Clock()
running = True
dt = 0

sc = 7
balls = 10
score = 0 
character = "bjorn"
multiplier = 0
shotScore = 0
feverMode = False
aim = 1
shotPoint=(96/2,200)
canFire = True            
availableBalls = 10

def rotate(angle,val):
   angle+=val
   if angle<-math.pi:
      angle=math.pi-(abs(angle)-math.pi)
   elif angle>math.pi:
      angle=-math.pi+(angle-math.pi)
   return angle


while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "blue", (96/2*sc,0), 5*sc)
    pygame.draw.line(screen, "blue", (96/2*sc,5*sc), (96/2*sc+aim,10*sc), 10)
    pygame.draw.rect(screen,(80,80,80),Rect(shotPoint[0]-15,150,30,50),0)
    
    pygame.draw.polygon(screen,(80,80,80),[(shotPoint[0]-math.cos(aim+math.pi/2)*15,shotPoint[1]-math.sin(aim+math.pi/2)*15),
                                 (shotPoint[0]+math.cos(aim+math.pi/2)*15,shotPoint[1]+math.sin(aim+math.pi/2)*15),
                                 (shotPoint[0]+math.cos(aim+math.pi/2)*15-math.cos(aim)*50,shotPoint[1]+math.sin(aim+math.pi/2)*15-math.sin(aim)*50),
                                 (shotPoint[0]-math.cos(aim+math.pi/2)*15-math.cos(aim)*50,shotPoint[1]-math.sin(aim+math.pi/2)*15-math.sin(aim)*50),],0)
    pygame.draw.circle(screen,(130,130,130),(int(shotPoint[0]),int(shotPoint[1])),30,0)

    keys = pygame.key.get_pressed()
    if  aim > -50:
        if keys[pygame.K_a]:
                aim -= 20 * dt
    if aim < 50:
        if keys[pygame.K_d]:
            aim += 20 * dt
          
    m = pygame.mouse.get_pos()
    aim=math.atan2(shotPoint[1]-m[1],shotPoint[0]-m[0])
    if aim>0 and aim<=math.pi/2:
      aim=0
    if aim>math.pi/2 and aim<math.pi:
      aim=math.pi
    aim=rotate(rotate(aim,math.pi/2)*1.2,-math.pi/2)
    if canFire and availableBalls>0:
      if pygame.mouse.get_pressed()[0]:
         canFire=False
         availableBalls-=1
         if availableBalls<0:
            availableBalls=0
         startPoint=(shotPoint[0]-math.cos(aim)*40,shotPoint[1]-math.sin(aim)*40)
         vel=(-math.cos(aim)*10,-math.sin(aim)*10)
 #        if specialShots>0:
  #         balls.append(ball(startPoint,vel,ability))
  #       else:                               
   #         balls.append(ball(startPoint,vel,"none"))

              


   
    pygame.display.update()
    pygame.display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
