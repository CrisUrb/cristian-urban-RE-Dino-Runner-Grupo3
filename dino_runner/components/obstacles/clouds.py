from dino_runner.utils.constants import (SCREEN_WIDTH)
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CLOUD

class Clouds:
    def __init__(self):
        self.image = CLOUD
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH 
        self.rect.y = 60
        self.index = 0 

    def update(self, game_speed):
        self.rect.x -= game_speed  #vel de acuerdo a la vel del juego

    def draw(self, screen):
        self.screen = screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.x <= -SCREEN_WIDTH:
            self.reset_values_cloud(self.screen)

    def reset_values_cloud(self, screen):
        self.rect.x = SCREEN_WIDTH 
        self.rect.y = 60
        self.draw(self.screen)

            

    