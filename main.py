import pygame
import os
from modules.vector2D import Vector2
from modules.star import Star
from modules.drawable import Drawable
from modules.backgrounds import *
from modules.animated import *
from modules.animatedOnce import *
import random
from modules.soundManager import SoundManager

SCREEN_SIZE = (400, 400)
WORLD_SIZE = (4000, 400)

SCALE = 2

UPSCALED = [x * SCALE for x in SCREEN_SIZE]

def main():

   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Space Dash")
   
   screen = pygame.display.set_mode(UPSCALED)
   drawSurf = pygame.Surface(SCREEN_SIZE)

   #incremented variables
   level = 0
   explos = 0
   
   #music
   mainSong = pygame.mixer.Sound('music/theme.wav')
   endSong = pygame.mixer.Sound('music/sunny.wav')
   crash = pygame.mixer.Sound('music/crash.wav')
   mainSong.play(-1)
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   spaceship = Star((110,130), "spaceship.png")
   explosion = Drawable("explosion2.png",(0,500))
   randint1 = random.randint(400, 500)
   randint2 = random.randint(90, 130)
   randint4 = random.randint(50, 80)

   #animations
   animatedEarth = AnimatedOnce("earthsprite.png", (0,0), 14)
   spaceshipExplode = AnimatedOnce("explosion.png", (400,120), 6)
   meteor1 = Animated("meteor1.png", (0,500), 4)
   meteor2 = Animated("meteor2.png", (0,500), 4)
   meteor3 = Animated("meteor3.png", (0,500), 4)
   meteor4 = Animated("meteor4.png", (0,500), 4)
   meteor5 = Animated("meteor1.png", (0,500), 4)
   meteor6 = Animated("meteor2.png", (0,500), 4)
   meteor7 = Animated("meteor3.png", (0,500), 4)
   meteor8 = Animated("meteor4.png", (0,500), 4)
   meteor9 = Animated("meteor1.png", (0,500), 4)
   meteor10 = Animated("meteor2.png", (0,500), 4)
   meteor11 = Animated("meteor3.png", (0,500), 4)
   meteor12 = Animated("meteor4.png", (0,500), 4)
   meteor13 = Animated("meteor1.png", (0,500), 4)
   meteor14 = Animated("meteor2.png", (0,500), 4)
   meteor15 = Animated("meteor1.png", (0,500), 4)
   satallite = Animated("satallite.png", (0,500), 4)
   satallite2 = Animated("satallite.png", (0,500), 4)
   meteorMove = Star((4000,120), "meteor4move.png")
   meteorMove2 = Star((4000,150), "meteor4move.png")
   satalliteMove = Star((7500,120), "satallite2.png")
   level1list = [meteor1, meteor2, meteor3, meteor4, meteor5, meteor6, meteor7, meteor8, meteor9, meteor10, meteor11]
   level2list = [meteor1, meteor2, meteor3, meteor4, meteor5, meteor6, meteor7, meteor8, meteor9, meteor10, meteor11]
   level3list = [meteor1, meteor2, meteor3, meteor4, meteor5, meteor6, meteor7, meteor8, satallite, meteor9, meteor10, meteor11]
   level4list = [meteor1, meteor2, meteor3, meteor4, meteor5, meteor6, meteor7, meteor8, meteor9, meteor10, meteor11, meteor12, satallite, meteor13, meteor14, satallite2, meteor15]
   #begin by shuffling lists
   random.shuffle(level1list)
   random.shuffle(level2list)
   random.shuffle(level3list)
   random.shuffle(level4list)

   #levels
   def mars():
      staticBG = RepeatingBackground(pygame.Rect(0,0,WORLD_SIZE[0],WORLD_SIZE[1]), "mars1.png", (0,0), None, 0)
      bg1 = RepeatingBackground(pygame.Rect(0,0,WORLD_SIZE[0],WORLD_SIZE[1]), "mars2.png", (0,0), None, 0.25)
      bg2 = RepeatingBackground(pygame.Rect(0,0,WORLD_SIZE[0],WORLD_SIZE[1]), "mars3.png", (0,0), None, 0.5)
      currentFloor = Floor("marsfloor.png", (0,320))
      staticBG.draw(drawSurf)
      bg1.draw(drawSurf)
      bg2.draw(drawSurf)
      currentFloor.draw(drawSurf)
      meteorMove.setVelocity(-200)
      meteorMove.draw(drawSurf)
      i = 0
      x = 0
      for hazard in level1list:
         if i%2==0:
            hazard.setPosition((randint1+x,randint2+75))
         else:
            hazard.setPosition((randint1+x,randint2-75))
         hazard.draw(drawSurf)
         i+=1
         x+=450
      
   def moon():
      staticBG = RepeatingBackground(pygame.Rect(0,0,WORLD_SIZE[0],WORLD_SIZE[1]), "moon-background.png", (0,0), None, 0)
      bg1 = Floor("moonfloor.png", (0,320))
      staticBG.draw(drawSurf)
      bg1.draw(drawSurf)
      i = 0
      x = 0
      meteorMove.setVelocity(-250)
      meteorMove.draw(drawSurf)
      for hazard in level2list:
         if i%2==0:
            hazard.setPosition((randint1+x,randint2-randint4))
         else:
            hazard.setPosition((randint1+x,randint2+randint4))
         hazard.draw(drawSurf)
         x+=400
         i+=1
      
         
   def saturn():
      slowBG = RepeatingBackground(pygame.Rect(0,0,WORLD_SIZE[0],WORLD_SIZE[1]), "saturnbackground.png", (0,0), None, .1)
      bg1 = RepeatingBackground(pygame.Rect(0,0,WORLD_SIZE[0],WORLD_SIZE[1]), "clouds1.png", (0,0), None, 0.25)
      bg2 = Floor("saturnfloor.png", (0,320))
      slowBG.draw(drawSurf)
      bg1.draw(drawSurf)
      bg2.draw(drawSurf)
      i = 0
      x = 0
      meteorMove.setVelocity(-300)
      meteorMove.draw(drawSurf)
      for hazard in level3list:
         if i%2==0:
            hazard.setPosition((randint1+x,randint2+randint4))
         else:
            hazard.setPosition((randint1+x,randint2-randint4))
         hazard.draw(drawSurf)
         i+=1
         x+=300

   def lastlevel():
      slowBG = RepeatingBackground(pygame.Rect(0,0,WORLD_SIZE[0],WORLD_SIZE[1]), "lastlevel.png", (0,0), None, 1)
      slowBG.draw(drawSurf)
      i = 0
      x = 0
      meteorMove.setVelocity(-400)
      meteorMove.draw(drawSurf)
      meteorMove2.setVelocity(-200)
      meteorMove2.draw(drawSurf)
      satalliteMove.setVelocity(-400)
      satalliteMove.draw(drawSurf)
      for hazard in level4list:
         if i%2==0:
            hazard.setPosition((randint1+x,randint2+randint4+30))
         else:
            hazard.setPosition((randint1+x,randint2-randint4))
         hazard.draw(drawSurf)
         i+=1
         x+=200

   def shuffleObjects():
      random.shuffle(level1list)
      random.shuffle(level2list)
      random.shuffle(level3list)
      random.shuffle(level4list)

   def drawLevel():
      if level == 0:
         mars()
         spaceship.setVelocity(300)
      elif level == 1:
         moon()
         spaceship.setVelocity(330)
      elif level == 2:
         saturn()
         spaceship.setVelocity(380)
      elif level == 3:
         lastlevel()
         spaceship.setVelocity(420)
      spaceship.draw(drawSurf)
      
   def drawEarth():
      animatedEarth.draw(drawSurf)

   def postCollision():
      meteorMove.resetPosition(4000, 120)
      meteorMove2.resetPosition(4000, 150)
      satalliteMove.resetPosition(7500, 120)
      spaceship.reset()
      spaceship.resetVelocity()
      drawLevel()
      
      
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:

      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      
      # Draw everything
      drawSurf.fill((30,30,30))

      #collision/shuffle
      if explos == 2:
         shuffleObjects()
         explos = 0
         crash.play(0)
      if explos == 1:
         postCollision()
         explos += 1
         crash.stop()
            
      # Check level
      if spaceship.getX()>WORLD_SIZE[0]-40:
         level += 1
         spaceship.resetPosition()
         spaceship.resetVelocity()
         for meteor in level1list:
            meteor.resetPosition(0,500)
         for hazard in level2list:
            hazard.resetPosition(0,500)
         for hazard in level3list:
            hazard.resetPosition(0,500)
         for hazard in level4list:
            hazard.resetPosition(0,500)
         meteorMove.resetPosition(3000, 120)

      #draw level
      drawLevel()
      if level > 3:
         drawEarth()
         mainSong.stop()
         endSong.play(0)

      # Detect collision
      bigList = level1list + level2list + level3list + level4list
      for hazard in bigList:
         if spaceship.getCollisionBox(5).colliderect(hazard.getCollisionBox(30)) or spaceship.getCollisionBox(5).colliderect(meteorMove.getCollisionBox(40))or spaceship.getCollisionBox(5).colliderect(meteorMove2.getCollisionBox(40))or spaceship.getCollisionBox(5).colliderect(satalliteMove.getCollisionBox(20)):
            explosion.setPosition((spaceship.getX()+10,spaceship.getY()))
            explosion.draw(drawSurf)
            explos=1
            
            
         
      pygame.transform.scale(drawSurf, UPSCALED, screen)
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         spaceship.handleEvent(event)
            
      # Get some time in seconds
      ticks = min(0.5, gameClock.get_time() / 1000)
      
      
      # Update everything
      if level > 3:
         animatedEarth.update(ticks)
      spaceship.update(ticks, WORLD_SIZE)
      spaceshipExplode.update(ticks)
      for meteor in level1list:
         meteor.update(ticks)
      for hazard in level2list:
         hazard.update(ticks)
      for hazard in level3list:
         hazard.update(ticks)
      for hazard in level4list:
         hazard.update(ticks)
      meteorMove.update(ticks, WORLD_SIZE)
      meteorMove2.update(ticks, WORLD_SIZE)
      satalliteMove.update(ticks, WORLD_SIZE)
      
      #earth level needs different offset
      if level != 4:
         Drawable.updateWindowOffset(spaceship, SCREEN_SIZE, WORLD_SIZE)
      else:
         Drawable.updateWindowOffset(spaceship, (SCREEN_SIZE[0],SCREEN_SIZE[1]), (4400-WORLD_SIZE[0],WORLD_SIZE[1]))
         

      
if __name__ == "__main__":
   main()
