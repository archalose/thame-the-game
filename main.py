import pygame
import os
from random import randrange, choice
from sys import exit
from time import sleep

pygame.init()

WIDTH, HEIGHT = 1600, 900
FPS = 60
clock = pygame.time.Clock()

ICON = pygame.image.load(os.path.join('assets', 'images', 'icon.png'))

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("thame the game")
pygame.display.set_icon(ICON)

CHARACTER_WIDTH = 90
CHARACTER_HEIGHT = 170

WHITE = 255, 255, 255
BLACK = 0, 0, 0

THAME_IMG_R = pygame.image.load(os.path.join('assets', 'images', 'thames_right.png'))

FACT_A_IMG = pygame.image.load(os.path.join('assets', 'images', 'fact_a.png'))
FACT_B_IMG = pygame.image.load(os.path.join('assets', 'images', 'fact_b.png'))
FACT_C_IMG = pygame.image.load(os.path.join('assets', 'images', 'fact_c.png'))
INSTRUCTION_IMG = pygame.image.load(os.path.join('assets', 'images', 'instruction.png'))
OBJECTIVE_IMG = pygame.image.load(os.path.join('assets', 'images', 'objective.png'))
MARZALEK_IMG = pygame.image.load(os.path.join('assets', 'images', 'marzalek.png'))


AXE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'axe.png')), (200, 200))
VICTOR_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'victor.png')), (200, 200))
VALORANT_IMG =  pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'valorant.png')), (200, 200))

JOHN_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'john_coltrane.jpg')), (500, 500))

M4A4_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images',  'm4a4.png')), (200, 200))
FLASH_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'flashbang.png')), (200, 200))
LICC_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'licc.png')), (200, 200))

THAME_RIGHT = pygame.transform.scale(THAME_IMG_R, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

font = pygame.font.Font(os.path.join('assets', 'fonts', 'comic.ttf'), 28)
font_bold = pygame.font.Font(os.path.join('assets', 'fonts', 'comicbd.ttf'), 48)



class Player:

    def __init__(self, health, velocity, character):
        self.health = health
        self.velocity = velocity
        self.character = character

    def movement_handler(self, keys_pressed):
        character = self.character
        
        if keys_pressed[pygame.K_a] and character.x - self.velocity > 0:
            character.x -= self.velocity

        if keys_pressed[pygame.K_d] and character.x + self.velocity + CHARACTER_WIDTH < WIDTH:
            character.x += self.velocity

        if keys_pressed[pygame.K_w] and character.y - self.velocity > 0:
            character.y -= self.velocity

        if keys_pressed[pygame.K_s] and character.y + self.velocity + CHARACTER_HEIGHT < HEIGHT:    
            character.y += self.velocity

    def heal(self, point=5):
        if self.health + point <= 10:
            self.health += point

    def detect_collisions(self, entity_list):
        character = self.character

        for entity in entity_list:
            if character.colliderect(entity):
                self.health -= 5




class Level:
    def __init__(self, name, description, hit_box):
        self.name = name
        self.description = description
        self.hit_box = hit_box

        window.fill(WHITE)
        window.blit(THAME_RIGHT, (hit_box.x, hit_box.y))   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()

    def clear_level(self):
        hit_box = self.hit_box
        window.fill(WHITE)
        window.blit(THAME_RIGHT, (hit_box.x, hit_box.y))   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()

    def title(self):
        text = font_bold.render(self.name, True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        window.blit(text, text_rect)

    def sub_heading(self):
        text = font.render(self.description, True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, (HEIGHT // 2) + 50)
        window.blit(text, text_rect)


def e_movement(entity_list, vel=5):
    for entity in entity_list:
        entity.x -= vel


def render_text(str, x, y, font=font):
    text = font.render(str, True, BLACK)
    window.blit(text, (x, y))


def spawn_enemies(ent_list, enemy_num):
    enemies_list = []
    img_list = []

    for i in range(enemy_num):
        img = choice(ent_list)
        entity = pygame.Rect(WIDTH + i * 600, randrange(99, HEIGHT - 200), 100, 100)

        enemies_list.append(entity)
        img_list.append(img)

    return enemies_list, img_list

def draw_enemies(enemies_list, img_list):
    
    for enemy in enemies_list:
        index = enemies_list.index(enemy)
        window.blit(img_list[index], enemy)   




def main():

    level_num = 0
    thame_hit_box = pygame.Rect(WIDTH // 2 - CHARACTER_WIDTH, HEIGHT - CHARACTER_HEIGHT, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    thame = Player(10, 10, thame_hit_box)
    

    while True:

        if level_num == 0:
            pygame.mixer.music.load(os.path.join('assets', 'music', 'winged_hussars.mp3'))
            pygame.mixer.music.play()

            thame.heal(10)

            while True:
                clock.tick(FPS) 

                main_menu = Level("thame the game", "press enter to continue, after this epic music of course", thame_hit_box)
                main_menu.title()
                main_menu.sub_heading()
                keys_pressed = pygame.key.get_pressed()
                thame.movement_handler(keys_pressed)

                if keys_pressed[pygame.K_RETURN]:
                    pygame.mixer.music.fadeout(2000)
                    level_num += 1
                    break

                pygame.display.update()

    
        if level_num == 1:
            pygame.mixer.music.load(os.path.join('assets', 'music', 'polish_cow.mp3'))
            pygame.mixer.music.play()

            clock.tick(FPS)
            level_one = Level("chapter 1:", "my name thame", thame_hit_box)
            level_one.title()
            level_one.sub_heading()
            pygame.display.update()

            fact_a_box, fact_b_box, fact_c_box \
            = pygame.Rect(WIDTH, 32, 600, 700), pygame.Rect(WIDTH + 1200, 400, 600, 700), pygame.Rect(WIDTH + 2200, 800, 600, 700)

            instruction_box, objective_box = pygame.Rect(WIDTH + 4000, 50, 600, 700), pygame.Rect(WIDTH + 6000, 600, 600, 700)
            
            
            sleep(2)
            while True:
                
                level_one.clear_level()
                clock.tick(FPS)
                keys_pressed = pygame.key.get_pressed()
                thame.movement_handler(keys_pressed)

                msg_list = [fact_a_box, fact_b_box, fact_c_box, instruction_box, objective_box]

                e_movement(msg_list)
                window.blit(FACT_A_IMG, (fact_a_box.x, fact_a_box.y))
                window.blit(FACT_B_IMG, (fact_b_box.x, fact_b_box.y))
                window.blit(FACT_C_IMG, (fact_c_box.x, fact_c_box.y))
                window.blit(INSTRUCTION_IMG, (instruction_box.x, instruction_box.y))
                window.blit(OBJECTIVE_IMG, (objective_box.x, objective_box.y))

                if objective_box.x == -1000:
                    pygame.mixer.music.fadeout(2000)
                    level_num += 1
                    break

                pygame.display.update()
        
        if level_num == 2:
            pygame.mixer.music.load(os.path.join('assets', 'music', 'uprising.mp3'))
            pygame.mixer.music.play()

            level_two = Level("chapter 2:", "the marzalek", thame_hit_box)
            level_two.title()
            level_two.sub_heading()
            pygame.display.update()
            sleep(2)

            level_two.clear_level()
            window.blit(MARZALEK_IMG, (900, 100))
            pygame.display.update()
            sleep(2)

            render_text("Marzalek? What are you doing here?", thame_hit_box.x - 90, thame_hit_box.y + 200)
            pygame.display.update()
            sleep(2)

            level_two.clear_level()
            window.blit(MARZALEK_IMG, (900, 100))
            render_text("I need your help thame. Poland has been invaded", 800, 700)
            pygame.display.update()
            sleep(2)

            level_two.clear_level()
            window.blit(MARZALEK_IMG, (900, 100))
            render_text("by who? the Germans?", thame_hit_box.x - 90, thame_hit_box.y + 200)
            pygame.display.update()
            sleep(2)

            level_two.clear_level()
            window.blit(MARZALEK_IMG, (900, 100))
            render_text("no, by a mysterious dark force", 850, 700)
            pygame.display.update()
            sleep(3)

            level_two.clear_level()
            window.blit(MARZALEK_IMG, (900, 100))
            render_text("I must go now, but come find me.", 850, 700)
            pygame.display.update()
            sleep(3)

            level_two.clear_level()
            window.blit(MARZALEK_IMG, (900, 100))
            render_text("and be careful young soldier", 850, 700)
            pygame.display.update()
            sleep(3)


            entities_imgs = [VICTOR_IMG, AXE_IMG, VALORANT_IMG]
            enemies_list, img_list = spawn_enemies(entities_imgs, 25)
            last_enemy = enemies_list[-1]

                
            while True:

                level_two.clear_level()
                clock.tick(FPS)
                keys_pressed = pygame.key.get_pressed()
                thame.movement_handler(keys_pressed)
                
                e_movement(enemies_list, randrange(8, 16))
                draw_enemies(enemies_list, img_list)
                thame.detect_collisions(enemies_list)

                if thame.health <= 0:
                    lose = True
                    break


                if last_enemy.x <= -1000:
            
                    pygame.mixer.music.load(os.path.join('assets', 'music', 'pilsudkis_death.mp3'))
                    pygame.mixer.music.play()

                    sleep(26)

                    level_two.clear_level()
                    window.blit(JOHN_IMG, (900, 100))
                    render_text("you fool! you couldn't save your beloved marzalek", 850, 700)
                    pygame.display.update()
                    sleep(3)

                    level_two.clear_level()
                    window.blit(JOHN_IMG, (900, 100))
                    render_text("what? how dare you kill MARZALEK!!", thame_hit_box.x - 90, thame_hit_box.y + 200)
                    pygame.display.update()
                    sleep(2)

                    level_two.clear_level()
                    window.blit(JOHN_IMG, (900, 100))
                    render_text("i will avenge your death marzalek", thame_hit_box.x - 90, thame_hit_box.y + 200)
                    pygame.display.update()
                    sleep(2)

                    level_two.clear_level()
                    window.blit(JOHN_IMG, (900, 100))
                    render_text("i won't go so easy on you this time", 850, 700)
                    pygame.display.update()
                    sleep(2)

                    level_num += 1
                    break

                pygame.display.update()

            
                
        if level_num == 3:
            pygame.mixer.music.load(os.path.join('assets', 'music', 'giant_steps.mp3'))
            pygame.mixer.music.play()

            sleep(3)

            clock.tick(FPS)
            level_three = Level("final chapter:", "for marzalek", thame_hit_box)
            level_three.title()
            level_three.sub_heading()
            pygame.display.update()

            sleep(2)

            entities_imgs = [VICTOR_IMG, AXE_IMG, VALORANT_IMG, M4A4_IMG, LICC_IMG, FLASH_IMG]
            enemies_list, img_list = spawn_enemies(entities_imgs, 50)
            last_enemy = enemies_list[-1]

            while True:
                level_three.clear_level()
                clock.tick(FPS)
                keys_pressed = pygame.key.get_pressed()
                thame.movement_handler(keys_pressed)

                e_movement(enemies_list, randrange(8, 21))
                draw_enemies(enemies_list, img_list)
                thame.detect_collisions(enemies_list)

                if thame.health <= 0:
                    lose = True
                    break

                if last_enemy.x <= -1000:
                    pygame.mixer.music.fadeout(2000)

                    level_two.clear_level()
                    window.blit(JOHN_IMG, (900, 100))
                    render_text("impossible! you win this time", 850, 700)
                    pygame.display.update()
                    sleep(3)

                    level_two.clear_level()
                    window.blit(JOHN_IMG, (900, 100))
                    render_text("but surely without a marzalek, polska will crumble", 850, 700)
                    pygame.display.update()
                    sleep(3)

                    level_two.clear_level()
                    window.blit(JOHN_IMG, (900, 100))
                    render_text("in no time i will be back", 850, 700)
                    pygame.display.update()
                    sleep(3)

                    level_two.clear_level()
                    render_text("i must become marzalek", thame_hit_box.x - 90, thame_hit_box.y + 200)
                    pygame.display.update()
                    sleep(2)
                    
                    level_two.clear_level()
                    render_text("dla polski!", thame_hit_box.x - 90, thame_hit_box.y + 200)
                    pygame.display.update()
                    sleep(2)

                    level_num += 1
                    break
                
                pygame.display.update()

        if level_num == 4:
            level_three.clear_level()
            pygame.mixer.music.load(os.path.join('assets', 'music', 'rick_roll.mp3'))
            pygame.mixer.music.play()

            window.fill(WHITE)
            render_text("directed by:", WIDTH - 1000, HEIGHT // 2, font_bold)
            pygame.display.update()
            sleep(0.5)
            render_text("phi", WIDTH - 1000, (HEIGHT // 2) + 70)
            pygame.display.update()
            sleep(3)

            window.fill(WHITE)
            render_text("storyline by:", WIDTH - 1000, HEIGHT // 2, font_bold)
            pygame.display.update()
            sleep(0.5)
            render_text("phi", WIDTH - 1000, (HEIGHT // 2) + 70)
            pygame.display.update() 
            sleep(3)

            window.fill(WHITE)
            render_text("art by:", WIDTH - 1000, HEIGHT // 2, font_bold)
            pygame.display.update()
            sleep(0.5)
            render_text("phi, and google", WIDTH - 1000, (HEIGHT // 2) + 70)
            pygame.display.update()
            sleep(3)               

            window.fill(WHITE)
            render_text("produced by:", WIDTH - 1000, HEIGHT // 2, font_bold)
            pygame.display.update()
            sleep(0.5)
            render_text("phi", WIDTH - 1000, (HEIGHT // 2) + 70)
            pygame.display.update()
            sleep(4)

            window.fill(WHITE)
            render_text("based on life of:", WIDTH - 1000, HEIGHT // 2, font_bold)
            pygame.display.update()
            sleep(0.5)
            render_text("thames", WIDTH - 1000, (HEIGHT // 2) + 70)
            pygame.display.update()
            sleep(3)

            window.fill(WHITE)
            render_text("special guest stars:", WIDTH - 1000, HEIGHT // 2, font_bold)
            pygame.display.update()
            sleep(0.5)
            render_text("victor, marzalek pilsudski, john coltrane", WIDTH - 1000, (HEIGHT // 2) + 70)
            pygame.display.update()
            sleep(3)

            window.fill(WHITE)
            render_text("happy birthday Thames", WIDTH - 1000, HEIGHT // 2, font_bold)
            pygame.display.update()

            pygame.mixer.music.fadeout(3000)
            sleep(5)

            window.fill(WHITE)
            render_text("thames will return", WIDTH - 1000, HEIGHT // 2, font_bold)
            pygame.display.update()
            sleep(2.5)

            pygame.display.quit()
            exit()



        if lose:

            end_messages = ["bruh what a bad", "thame is mister bad afterall", "404 error, skill not found", "can't sig your way out of this now can you"]
            game_over = Level(choice(end_messages), "press enter to restart", thame_hit_box)
            game_over.title()
            pygame.display.update()
            sleep(1)
            game_over.sub_heading()
            pygame.display.update()

            while True:
                clock.tick(FPS)
                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_RETURN]:
                    lose = False
                    thame.heal(10)
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.quit()
                        exit()
                
                pygame.display.update()



            

            

        




if __name__ == '__main__':
    main()



