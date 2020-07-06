import pygame
from pygame import image
import os
from .frameManager import FRAMES
from .drawable import Drawable

class Animated(Drawable):
   
   def __init__(self, imageName, position, nFrames):
      super().__init__(imageName, position, (0,0))

      self._imageName = imageName
      self._position = position
      self._frame = 0
      self._row = 0
      self._animationTimer = 0
      self._framesPerSecond = 10.0
      self._nFrames = nFrames
      
      self._animate = True
      

      
   def update(self, ticks):
      if self._animate:
         self._animationTimer += ticks
         
         if self._animationTimer > 1 / self._framesPerSecond:
            self._frame += 1
            self._frame %= self._nFrames
            self._animationTimer -= 1 / self._framesPerSecond
            self._image = FRAMES.getFrame(self._imageName, (self._frame, self._row))
         
   def resetFrame(self):
      self._frame = 0
   
   def startAnimation(self):
      self._animate = True
   
   
   def stopAnimation(self):
      self._animate = False

   def copy(self):
      copy = self.__init__(self._imageName, self._position, self._nFrames)
      return copy
