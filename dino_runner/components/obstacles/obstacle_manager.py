import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird
from dino_runner.utils.constants import(SMALL_CACTUS, LARGE_CACTUS, BIRD)


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles)==0:
            cactus_size = random.randint(0,1)  # generamos los cactus grandes y pequeños
            if cactus_size == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.hammer is not None and game.player.hammer.rect.colliderect(obstacle):#colision con el martillo 
                game.player.hammer.kill()
                self.obstacles.pop()
            else:
                obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):    #Cuando el dino choca lo detecta con colliderect
                if not game.player.shield:
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player_show_text = False 
                        game.player.shield = True
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000

                    else:
                        #pygame.time.delay(100)
                        game.playing = False
                        game.death_count += 1
                        break
                else:
                    self.obstacles.remove(obstacle)
            

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            

    def reset_obstacles(self, self1):
        self.obstacles = []


