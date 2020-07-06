from .frameManager import FrameManager
from .drawable import Drawable
from .vector2D import Vector2
import pygame
from .animatedOnce import AnimatedOnce
from .animated import Animated


class Star(Drawable):
   def __init__(self, position, fileName):
      self._velocity = Vector2(0,0)
      self.position = position
      self._movement = { pygame.K_UP: False,
                         pygame.K_DOWN: False,
                         pygame.K_LEFT: False,
                         pygame.K_RIGHT: False
                        }
      super().__init__(fileName, position)
      self.image = super().getImage()
      self._isDead = False
      
      
   def handleEvent(self, event):
      if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
         if event.key in self._movement.keys():
            self._movement[event.key] = (event.type == pygame.KEYDOWN)

   def resetVelocity(self):
      self._velocity = Vector2(0,0)

   def setVelocity(self, velocityx):
      self._velocity[0] = velocityx

   def setExplosion(self):
      self.__init__(self.getPosition(), "explosion2.png")
      
   def update(self, ticks, worldInfo):
      if self._movement[pygame.K_UP]:
         self._velocity[1] = -100
      elif self._movement[pygame.K_DOWN]:
         self._velocity[1] = 100
         
      distanceVector = self._velocity * ticks 
      newPosition = self.getPosition() + distanceVector
      
      if newPosition[1] + self.getSize()[1] > worldInfo[1] - 80 or  newPosition[1] < 0:
            self._velocity[1] = -self._velocity[1]            
            distanceVector = self._velocity * ticks
            newPosition = self.getPosition() + distanceVector
      self.setPosition(newPosition)

      
   def isDead(self):
      self._isDead = True
      return self._isDead

   def reset(self):
      self.__init__((0,130), "spaceship.png")
      self._isDead = False
      
             
         
   
   
      
