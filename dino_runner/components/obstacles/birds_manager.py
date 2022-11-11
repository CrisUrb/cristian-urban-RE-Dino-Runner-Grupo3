import pygame
import random

from dino_runner.components.obstacles.birds import Bird
from dino_runner.utils.constants import BIRD


class BirdsManager:
    def __init__(self):
        self.birds = []
        self.index = 0

    def update(self, game):

        bird_appears = random.randint(0,100)
        if len(self.birds)==0 and bird_appears % 4 == 0:
            #bird_appears = random.randint(0,100)  # generamos los aves en numeros random
            self.birds.append(Bird())

            
        for bird in self.birds:
            #while len(self.birds)==0: 
            bird.update(game.game_speed, self.birds) 
             
            if game.player.hammer is not None and game.player.hammer.rect.colliderect(bird):#colision con el martillo 
                game.player.hammer.kill()
                self.birds.pop()
            else:
                bird.update(game.game_speed, self.birds)

            if game.player.dino_rect.colliderect(bird.rect):    #Cuando el dino choca lo detecta con colliderect
                if not game.player.shield:
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player_show_text = False 
                        game.player.shield = True
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000

                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                else:
                    self.birds.remove(bird)
           

    def draw(self, screen):
        for bird in self.birds:
            bird.draw(screen)

    def reset_obstacles(self, self1):
        self.birds = []

