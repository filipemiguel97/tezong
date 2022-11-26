import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.color = color
        self.width = width
        self.height = height
        
        # Pass in the color of the Paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
        self.isFire = False
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y > 400:
          self.rect.y = 400
    
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0
          
    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > 690:
          self.rect.x = 690
    
    def setFire(self,setfire):
        self.isFire = setfire
        
        # Call the parent class (Sprite) constructor
        super().__init__()
                
        # Pass in the color of the Paddle, its width and height.
        # Set the background color and set it to be transparent
        # self.image = pygame.Surface([self.width, self.height])
        # self.image.fill(BLACK)
        # self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        # if setfire:
        #     pygame.draw.rect(self.image, (255,0,0), [self.rect.x, self.rect.y, self.rect.width , self.rect.height])
        # else:
        #     pygame.draw.rect(self.image, (0,0,0), [self.rect.x, self.rect.y, self.rect.width , self.rect.height])

        #self.rect = self.image.get_rect()               
            
        
    def isFire(self):
        return self.isFire
    
    
    