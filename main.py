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
                
        #alteR refresh
        screen.blit(background, (0, 0))
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
        
    