
from dino_runner.utils.constants import (SCREEN_WIDTH)
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird:
    def __init__(self):
        self.image = BIRD[0]
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH * 1.5
        self.rect.y = 90
        self.index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed  #vel de acuerdo a la vel del juego
        self.fly()
        if self.rect.x < -self.rect.width and obstacles:
            obstacles.pop()
        if self.index >= 10: 
            self.index = 0 


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    
    def fly(self):
        if self.index >= 10: 
            self.index = 0 
        
        if self.index < 5:
            self.image = BIRD[0]  
        else: 
            BIRD[1]
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y
        self.index += 1


    
