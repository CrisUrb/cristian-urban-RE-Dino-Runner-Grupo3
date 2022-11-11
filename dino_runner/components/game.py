import pygame

from dino_runner.components import text_untils
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.power_up_manager import PowerManager
from dino_runner.utils.constants import (BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,
                                         RUNNING, CLOUD, HAMMER_TYPE, SHIELD_TYPE, RESET)
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_hearts_manager import PlayerHeartManager
from dino_runner.components.obstacles.birds_manager import BirdsManager
from dino_runner.components.obstacles.clouds import Clouds

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player =  Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.power_up_manager = PowerManager()
        self.player_heart_manager = PlayerHeartManager()
        self.best_score = 0
        self.birds_manager = BirdsManager()
        self.clouds = Clouds()


    def run(self):
        self.create_components()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def create_components(self):

        self.obstacle_manager.reset_obstacles(self)
        self.birds_manager.reset_obstacles(self)
        self.player_heart_manager.reset_hearts()
        self.power_up_manager.reset_power_ups(self.points, self.player)
        self.player.update_to_default( RUNNING )
        self.player.update_to_default( HAMMER_TYPE )
        self.player.update_to_default( SHIELD_TYPE )

        self.points = 0
        self.game_speed = 15

       
    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False 
        self.screen.fill((255,255,255))

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.birds_manager.update(self)
        self.clouds.update(self.game_speed)


    def draw(self):
        self.score() #Muestra el score en tiempo real
        self.clock.tick(FPS)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.birds_manager.draw(self.screen)
        self.clouds.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):  #Fondo
        image_width = BG.get_width()
        self.screen.blit(BG,(self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG,(image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def score(self):

        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_untils.get_score_element(self.points)
        self.screen.blit(text, text_rect) #mostramos texto en pantalla del rectangulo
        self.player.check_in_invensibility(self.screen)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #SI PRESIONAMOS EL TACHE ROJO 
                self.running = False
                self.playing = False 
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:   #Cuando presionamos una tecla inicia el juego

                self.run()

    def print_menu_elements(self):
        half_creen_heigth = SCREEN_HEIGHT // 2
        half_creen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            text, text_rect = text_untils.get_centred_message('Press any key to start')
            self.screen.blit(text, text_rect)

        elif self.death_count > 0:
            if self.best_score < self.points:
                self.best_score = self.points
            text, text_rect = text_untils.get_centred_message('Press any key to Restart')
            score, score_rect = text_untils.get_centred_message('You score: '+ str(self.points), height = half_creen_heigth + 50)
            best_score, best_score_rect = text_untils.get_centred_message('You best score: '+ str(self.best_score), height = half_creen_heigth + 100)
            death, death_rect = text_untils.get_centred_message('Death count: '+ str(self.death_count), height = half_creen_heigth + 150)
            
            self.screen.blit(score, score_rect) #Blit muestra en pantalla
            self.screen.blit(best_score, best_score_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(death, death_rect)
            
            
            self.image = RESET
            self.rect = self.image.get_rect()
            self.rect.x = SCREEN_WIDTH // 2 - 40
            self.rect.y = SCREEN_HEIGHT // 1.25
            self.screen.blit(self.image, (self.rect.x, self.rect.y))

        self.screen.blit(RUNNING[0], (half_creen_width  -20, half_creen_heigth -140))

    def show_menu(self):
        self.running = True

        white_color = (255,255,255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()
