# develop a python game using pygame library which can be installed using pip
import pygame
import random
import time

class game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = player(self)
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.all_sprites.add(self.bullets)
        self.all_sprites.add(self.enemy_bullets)
        self.score = 0
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("Score: " + str(self.score), 1, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (400, 50)
        self.enemy_timer = 0
        self.enemy_timer_max = 100
        self.enemy_timer_max_2 = 100
        self.enemy_timer_max_3 = 100
        self.enemy_timer_max_4 = 100
        self.enemy_timer_max_5 = 100
        self.enemy_timer_max_6 = 100
        self.enemy_timer_max_7 = 100
        self.enemy_timer_max_8 = 100
        self.enemy_timer_max_9 = 100
        self.enemy_timer_max_10 = 100
        self.enemy_timer_max_11 = 100
        self.enemy_timer_max_12 = 100
        self.enemy_timer_max_13 = 100
        self.enemy_timer_max_14 = 100
        self.enemy_timer_max_15 = 100
        self.enemy_timer_max_16 = 100
        self.enemy_timer_max_17 = 100
        self.enemy_timer_max_18 = 100
        self.enemy_timer_max_19 = 100
        self.enemy_timer_max_20 = 100
        self.enemy_timer_max_21 = 100
        self.enemy_timer_max_22 = 100
        self.enemy_timer_max_23 = 100
        self.enemy_timer_max_24 = 100
        self.enemy_timer_max_25 = 100
        self.enemy_timer_max_26 = 100
        self.enemy_timer_max_27 = 100
        self.enemy_timer_max_28 = 100
        self.enemy_timer_max_29 = 100
        self.enemy_timer_max_30 = 100
        self.enemy_timer_max_31 = 100
        self.enemy_timer_max_32 = 100
        self.enemy_timer_max_33 = 100
        self.enemy_timer_max_34 = 100
        self.enemy_timer_max_35 = 100
        self.enemy_timer_max_36 = 100
        self.enemy_timer_max_37 = 100
        self.enemy_timer_max_38 = 100
        self.enemy_timer_max_39 = 100
        self.enemy_timer_max_40 = 100
        self.enemy_timer_max_41 = 100
        self.enemy_timer_max_42 = 100
        self.enemy_timer_max_43 = 100
        self.enemy_timer_max_44 = 100
        self.enemy_timer_max_45 = 100
        self.enemy_timer_max_46 = 100
        self.enemy_timer_max_47 = 100
        self.enemy_timer_max_48 = 100
        self.enemy_timer_max_49 = 100
        self.enemy_timer_max_50 = 100
        self.enemy_timer_max_51 = 100
        self.enemy_timer_max_52 = 100
        self.enemy_timer_max_53 = 100
        self.enemy_timer_max_54 = 100
        self.enemy_timer_max_55 = 100
        self.enemy_timer_max_56 = 100
        self.enemy_timer_max_57 = 100
        self.enemy_timer_max_58 = 100
        self.enemy_timer_max_59 = 100
        self.enemy_timer_max_60 = 100
        self.enemy_timer_max_61 = 100

    def run(self):
        pygame.sprite.get_sprites_from_layer()
        while self.running:
            pygame.surfarray.pixels_red ()
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        pygame.mixer.set_endevent()
        for event in pygame.event.get():
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                if event.key == pygame.K_RIGHT:
                    self.player.move_right()



                  
                  
    def enemy_type_1(self):
        if self.enemy_timer == 0:
            enemy_1 = enemy(self)
            self.enemies.add(enemy_1)
            self.all_sprites.add(enemy_1)
            self.enemy_timer = self.enemy_timer_max
        else:
            self.enemy_timer -= 1

    def enemy_type_2(self):
            if self.enemy_timer == 0:
                enemy_2 = enemy_2(self)
                self.enemies.add(enemy_2)
                self.all_sprites.add(enemy_2)
                self.enemy_timer = self.enemy_timer_max_2
            else:
                self.enemy_timer -= 1

    def enemy_type_3(self):
        if self.enemy_timer == 0:
            enemy_3 = enemy_3(self)
            self.enemies.add(enemy_3)
            self.all_sprites.add(enemy_3)
            self.enemy_timer = self.enemy_timer_max_3
        else:
            self.enemy_timer -= 1



    # run this game
    def update(self):
        self.all_sprites.update()
        elf.enemy_timer += 1
        if self.enemy_timer == self.enemy_timer_max:
                        self.enemy_timer = 0
                        self.enemy_timer_max = random.randint(100,200)
                        enemy_type = random.randint(1,3)
                        if enemy_type == 1:
                            enemy_type_1(self)
                        elif enemy_type == 2:
                            enemy_type_2(self)
                        elif enemy_type == 3:
                            enemy_type_3(self)
                    if self.enemy_timer == self.enemy_timer_max_2:
                        self.enemy_timer = 0
                        self.enemy_timer_max_2 = random.randint(100,200)
                        enemy_type = random.randint(1,3)
                        if enemy_type == 1:
                            enemy_type_1(self)
                        elif enemy_type == 2:
                            enemy_type_2(self)
                        elif enemy_type == 3:
                            enemy_type_3(self)
                    if self.enemy_timer == self.enemy_timer_max_3:
                        self.enemy_timer = 0
                        self.enemy_timer_max_3 = random.randint(100,200)
                        enemy_type = random.randint(1,3)
                        if enemy_type == 1:
                            enemy_type_1(self)
                        elif enemy_type == 2:
                            enemy_type_2(self)
                        elif enemy_type == 3:
                            enemy_type_3(self)
                    if self.enemy_timer == self.enemy_timer_max_4:
                        self.enemy_timer = 0
                        self.enemy_timer_max_4 = random.randint(100,200)
                        enemy_type = random.randint(1,3)
                        if enemy_type == 1:
                            enemy_type_1(self)
                        elif enemy_type == 2:
                            enemy_type_2(self)



            
            
        

  

        
