# -*- coding: utf-8 -*-

#power_ups is a dictionary
# power_ups = {'Fireball' : n, 'Lazers' : n, 'Barricades' : n}
# powerup_charge = {'Fireball' : 0, 'Lazers' : 0, 'Barricades' : 0}
powerup_charge_rate = {'Fireball' : 1.0, 'Lazers' : 0.01, 'Barricades' : 1.0}
import pygame
from paddle import Paddle
from Barricades import Barricade
import copy as cp
WHITE = (255,255,255)
from random import randint

class Player:
    
    def __init__(self,power_ups,name,paddle_pos):
        self.powerups = power_ups
        self.name = name
        
        self.powerup_charge = cp.copy(power_ups)
        self.powerup_charge = {x:0 for x in self.powerup_charge}
        
        # Initiate player's paddle
        self.paddle = Paddle(WHITE, 10, 100, paddle_pos)
        
        self.deployBarricade = False
        
        self.BarricadesList = pygame.sprite.Group()
        
    def getPowerupN(self,power_up):
        return self.powerups[power_up]
    
    def getChargeTime(self,power_up):
        return self.powerup_charge[power_up]
    
    def getName(self):
        return self.name
    
    def usePowerup(self,power_up):
        if self.powerups[power_up] > 0 and self.powerup_charge[power_up] == 100.0:
            self.powerups[power_up] -= 1
            self.powerup_charge[power_up] = 0
            print(power_up + '!!!')
            
            if power_up == 'Fireball':
                self.paddle.setFire(True)
            if power_up == 'Barricades':
                new_barricade = Barricade((155,255,155),randint(10,20),randint(80,120))
                new_barricade.deploy(randint(0,400),randint(0,400))
                self.BarricadesList.add(new_barricade)
    
    def chargePowerups(self):
        for powerup in self.powerups.keys():
            if self.powerup_charge[powerup] < 100.0:
                self.powerup_charge[powerup] += powerup_charge_rate[powerup]
                if self.powerup_charge[powerup] > 100.0:
                    self.powerup_charge[powerup] = 100.0
        #print(self.powerup_charge['Fireball'])
        self.deployBarricade = False
    
    def getPaddle(self):
        return self.paddle
    
    def moveUp(self,pixels):
        self.paddle.moveUp(pixels)
    def moveDown(self,pixels):
        self.paddle.moveDown(pixels)
    def moveLeft(self,pixels):
        self.paddle.moveLeft(pixels)
    def moveRight(self,pixels):
        self.paddle.moveRight(pixels)
    
    def getBarricades(self):
        return self.BarricadesList

        
        
        
    

#power_ups = {'Fireball' : 1, 'Lazers' : 0, 'Barricades' : 0}

#player1 = Player(power_ups,'Filipe')