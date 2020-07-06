import pygame
from pygame import *
from .frameManager import FrameManager
from .vector2D import Vector2
import os

class Drawable(object):
   
   WINDOW_OFFSET = [0,0]
   
   @classmethod
   def updateWindowOffset(cls, followObject, screenSize, worldSize):
      position = followObject.getPosition()
      Drawable.WINDOW_OFFSET = [min(max(0, position[x] - screenSize[x] // 2) + 100, worldSize[x] - screenSize[x]) for x in range(2)]

   @classmethod
   def adjustMousePos(cls, mousePos):
      ret = list(mousePos)
      ret[0] += Drawable.WINDOW_OFFSET[0]
      ret[1] += Drawable.WINDOW_OFFSET[1]
      return ret
   
   def __init__(self, imageName, position, offset=None, parallax=1):
      self.offset=offset
      self._imageName = imageName
      #if self._imageName != "":
      self._image = FrameManager.getInstance().getFrame(imageName, offset)
      self._worldBound = True
      self._position = Vector2(*position)
      self._parallax = parallax

   def getImage(self):
      return self._image
      
   def getPosition(self):
      return self._position
   
   def getX(self):
      return self._position[0]

   def getY(self):
      return self._position[1]

   def setPosition(self, newPosition):
      self._position = newPosition

   def resetPosition(self, x=70, y=120):
      self._position = Vector2(x,y)
      
   def getSize(self):
      return self._image.get_size()
   
   def getOffset(self):
      return self.offset

   def getCollisionBox(self, collision=10):
      newX = self._position[0] 
      newY = self._position[1]
      newRect =  pygame.Rect(newX+(collision), newY+(collision), self._image.get_width() - (collision*2), self._image.get_height() - (collision*2))
      return newRect

   def draw(self, surface):
      if self._worldBound:
         surface.blit(self._image, (int(self._position[0] - Drawable.WINDOW_OFFSET[0] * self._parallax),
                                    int(self._position[1] - Drawable.WINDOW_OFFSET[1] * self._parallax)))
      else:
         surface.blit(self._image, self._position)

