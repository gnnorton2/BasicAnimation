# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:41:08 2024

@author: gnoel
"""

import pygame
def main():
    #Important and Initialize Idea
    #already imported
    pygame.init()
    
    #iDea Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("You've got mail!")
    
    #idEa background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("background.png")
    
    #the sprite
    box = pygame.Surface((25, 25))
    box = box.convert()
    
    box = pygame.image.load("youveGotMail.png")
    
    #second Sprite
    box2 = pygame.Surface((25, 25))
    box2 = box.convert()
    
    box2 = pygame.image.load("youveGotMail.png")
    
    #third sprite
    box3 = pygame.Surface((25, 25))
    box3 = box.convert()
    
    box3 = pygame.image.load("youveGotMail.png")
    
    #image variables
    box_x = 0
    box_y = 200

    box2_x = 0
    box2_y = 0
    
    box3_x = 213 #426
    box3_y = 240
    #ideA Action Alter
    clock = pygame.time.Clock()
    keepGoing = True
    
    #aLter loop
    while keepGoing:
        #alTer Timer
        clock.tick(30) #fps
        
        #altEr Event haandling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #image values
        box_x += 5
        box_y += 2
        #boundaries
        if box_x > screen.get_width():
            box_x = 0
            
        if box_y > screen.get_height():
            box_y = 0
            
        box2_x += 2
        box2_y += 5
        
        if box2_x > screen.get_width():
            box2_x = 0
            
        if box2_y > screen.get_height():
            box2_y = 0
            
        box3_x += 3
        box3_y += 1
        
        if box3_x > 426:
            box3_x = 213
        if box3_y > screen.get_height():
            box3_y = 0
        #alteR refresh
        screen.blit(background, (0, 0))
        
        screen.blit(box, (box_x, box_y))
        screen.blit(box2, (box2_x, box2_y))
        screen.blit(box3, (box3_x, box3_y))
        
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
        
    