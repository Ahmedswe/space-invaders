
import random
import pygame
import sys
import time
pygame.init()


# creating a class that displays and manages screen and text

class screen():
    def __init__(self):
        self.screen_height = 650
        self.screen_width = 850
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.background_img = pygame.image.load(f"data\\bg.png")
        self.background_img = pygame.transform.scale(self.background_img, (self.screen_width, self.screen_height))
        self.gameover_img = pygame.image.load(f"data\\AquanoidGO.png")
        self.gameover_img = pygame.transform.smoothscale(self.gameover_img, (self.screen_width, self.screen_height))
        self.level = 0
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont(None, 30)
        self.white_color = (255, 255, 255)

    # a function for drawing screen

    def draw_screen(self):
        pygame.display.update()
        self.screen.blit(self.background_img, (0, 0))

    # a function for displaying score and level
    def display_score(self):
        score_text = self.font.render(
            f"score : {self.score}", True, self.white_color)
        self.screen.blit(score_text, (0, 0))
    def display_level(self):
        level_text = self.font.render(f"level : {self.level}", True, self.white_color)
        self.screen.blit(level_text, (self.screen_rect.midtop))

    # a function for displaying game over image

    def game_over(self):
        self.screen.blit(self.gameover_img, (0, 0))

    # function for displaying highscore and lives

    def display_highscore_and_lives(self, highscore):
        highscore_text = self.font.render(
            f"highscore : {highscore}", True, (255, 255, 255))
        self.screen.blit(highscore_text, (690, 0))
        lives_text = self.font.render(
            f"lives : {self.lives}", True, self.white_color)
        self.screen.blit(lives_text, (0, 630))
window = screen()




# a class that will manage the lasers


class lasers():
    def __init__(self, x, y, laser_img):
        self.x = x
        self.y = y
        self.laser_image = laser_img
        self.ship_laser_velocity = 5


    # a function for drawing lasers on screen
    def draw_ship_laser(self):
        window.screen.blit(self.laser_image, (self.x+13, self.y-25))
    # a function that will tell us if the laser is off the screen or not
    def off_screen(self):
        return not(self.y <= window.screen_height and self.y >= 0)

    # a function for moving the laser upward on the screen
    def move_ship_laser(self):
        self.y -= self.ship_laser_velocity


# a  class that controls and manages player ship and the lasers that the ship will fire

class player_ship():
    def __init__(self, x, y):
        self.ship_img = pygame.image.load("data\\spaceship.png")
        self.ship_img = pygame.transform.smoothscale(self.ship_img, (60, 60))
        self.ship_bullet = pygame.image.load(f"data\\ship_bullet.png")
        self.ship_bullet = pygame.transform.smoothscale(self.ship_bullet, (30, 30))
        self.ship_speed = 5
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.x = x
        self.y = y
        self.ship_lasers = []
        self.cool_down_counter = 0
        self.cool_down = 10

        # a function for drawing ship on screen and shooting the ship lasers

    def draw_ship_and_shoot_laser(self):
        window.screen.blit(self.ship_img, (self.x, self.y))
        for laser in self.ship_lasers:
            laser.draw_ship_laser()
            laser.move_ship_laser()
            if laser.off_screen():
                self.ship_lasers.remove(laser)

    # a function the will create the ship_laser and add it to the list every time space key is pressed
    def ship_laser(self):
        self.cool_down_counter += 1
        if  self.cool_down_counter >= self.cool_down:
            self.cool_down_counter = 0
        if self.cool_down_counter == 0:
            laser = lasers(self.x, self.y, self.ship_bullet)
            self.ship_lasers.append(laser)
 

    # a fuction for handling collision of laser with enemy and collision of enemy with ship it will
    # also increase score if an enemy is killed and also decreases a life if enemy collides with ship
    def laser_and_ship_collision_with_enemy(self, enemy, enemies):
        for laser in self.ship_lasers:
            if abs(laser.x - enemy.x) < 30 and abs(laser.y - enemy.y) < 60:
                enemy.health -= 1
                self.ship_lasers.remove(laser)
                if enemy.health == 0:
                    window.score += 10
                    enemies.remove(enemy)
        if abs(ship.x - enemy.x) < 50 and abs(ship.y - enemy.y) < 40:
            enemies.remove(enemy)
            window.lives -= 1


ship = player_ship(420, 580)


# loading and scaling  enemy images

yellow_enemy = pygame.image.load(f"data\\alien1.png")
yellow_enemy = pygame.transform.smoothscale(yellow_enemy, (50, 50))
blue_enemy = pygame.image.load("data\\alien5.png")
blue_enemy = pygame.transform.smoothscale(blue_enemy, (50, 50))
red_enemy = pygame.image.load("data\\alien4.png")
red_enemy = pygame.transform.smoothscale(red_enemy, (50, 50))
purple_enemy = pygame.image.load("data\\alien3.png")
purple_enemy = pygame.transform.smoothscale(purple_enemy, (50, 50))
white_enemy = pygame.image.load("data\\alien5.png")
white_enemy = pygame.transform.smoothscale(white_enemy,(50,50))

# creating a class for managing enemies


class Enemies():
    enemy_sequence = {"red": red_enemy,
                    "blue": blue_enemy,
                    "yellow":yellow_enemy,
                    "white":white_enemy,
                    "purple":purple_enemy}

    def __init__(self, x, y, color, health):
        self.x = x
        self.y = y
        self.health = health
        self.enemy_image = self.enemy_sequence[color]
        self.mask = pygame.mask.from_surface(self.enemy_image)
        self.enemy_velocity = 0.8
        self.enemy_lasers = []
        # a function that will move enemies downward on screen

    def move_enemy(self):
        self.y += self.enemy_velocity
        # a function the will draw the enemy

    def draw_enemy(self):
        window.screen.blit(self.enemy_image, (self.x, self.y))

                







def main_menu():
    font = pygame.font.SysFont("comicsans",50)
    title = font.render("press any  key to begin",True,window.white_color)
    while True:
        window.draw_screen()
        window.screen.blit(title,(150,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                else:
                    game_loop()
    
    
def game_loop():
    fps = 60
    clock = pygame.time.Clock()  # creating clock for game
    fleet_size = 5  # it will determine that how many enemies we will have at each level
    # it will determine that how many enemies will be added in the fleet at each level
    enemy_increase = 5
    enemy_boundry = -1500
    enemies = []
    # a variable that will make the game over when it changes to true from false
    game_over = False
    fire = False  # a variable that will let the bullet be shot only if its true
    path ="data\highscore.txt"
    with open(path, "r") as file:
        highscore = file.read()
# starting the actual game loop

    while True:
            window.draw_screen()  # drawing scre
            clock.tick(fps)
            window.display_score()  # displaying score and level
        # displaying highscroe and lives
            window.display_highscore_and_lives(highscore)
            window.display_level()

# updating highscore if score is greater then highscore
            if window.score > int(highscore):
                highscore = window.score
# writing the highscore to the file 
            with open(path, "r+") as file:
                file.write(str(highscore))


#  increasing the level and size of fleet with each level
            if len(enemies) == 0:
                window.level += 1
                window.display_level()
                fleet_size += enemy_increase
            # creating enemy and adding it to the list
                for i in range(fleet_size):
                    enemy = Enemies(random.randrange(0, window.screen_width-45), random.randrange(
                    enemy_boundry, -100), random.choice(["red", "blue", "white","blue","purple"]),random.randint(2,5))
                    enemies.append(enemy)

        # drawing each enemy moving it down the screen
            for enemy in enemies:
                enemy.draw_enemy()
                enemy.move_enemy()
                ship.laser_and_ship_collision_with_enemy(enemy, enemies)            
        # decreasing a life if the enemy reaches the bottom of screen
                if enemy.y  >= window.screen_height   :
                    window.lives -= 1
                    enemies.remove(enemy)

# responding to keypress

            for event in pygame.event.get():
            #  closing the game if close button is pressed
                if event.type == pygame.QUIT:
                    if window.score > int(highscore):
                        highscore = window.score
                        window.score = 0
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                # exiing the game if game is over and ecs is pressed
                    if event.key == pygame.K_ESCAPE and game_over:
                        sys.exit()
                # restarting the game if enter is pressed when game is over
                    if event.key == pygame.K_RETURN and game_over:
                        window.level = 0
                        window.lives = 5
                        enemies.clear()
                        game_over = False
                        game_loop()
                # making the movement variable true according to the keypress and making the other variables false
                    if event.key == pygame.K_RIGHT:
                        ship.move_right = True
                        ship.move_left = False
                        ship.move_up = False
                        ship.move_down = False
                    if event.key == pygame.K_LEFT:
                        ship.move_left = True
                        ship.move_right = False
                        ship.move_up = False
                        ship.move_down = False
                    if event.key == pygame.K_UP:
                        ship.move_up = True
                        ship.move_left = False
                        ship.move_right = False
                        ship.move_down = False
                    if event.key == pygame.K_DOWN:
                        ship.move_down = True
                        ship.move_left = False
                        ship.move_right = False
                        ship.move_up = False
                    if event.key == pygame.K_SPACE:
                        fire = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        ship.move_right = False
                    if event.key == pygame.K_LEFT:
                        ship.move_left = False
                    if event.key == pygame.K_UP:
                        ship.move_up = False
                    if event.key == pygame.K_DOWN:
                        ship.move_down = False
                    if event.key == pygame.K_SPACE:
                        fire = False
        # setting boundries for the ship and moving the ship according to the button pressed
            if ship.move_right and ship.x < window.screen_width - 60:
                ship.x += ship.ship_speed
            if ship.move_left and ship.x > 0:
                ship.x -= ship.ship_speed
            if ship.move_up and ship.y > 5:
                ship.y -= ship.ship_speed
            if ship.move_down and ship.y < window.screen_height - 60:
                ship.y += ship.ship_speed

        # here the fire variable  became true and lasers are being created while its true
            if fire:
                ship.ship_laser()

        # drawing ship and shoting lasers if space is pressed
            ship.draw_ship_and_shoot_laser()

        # adjusting the speed of ship and number of increase in enenies according to the increase of levels
            if window.level == 3:
                ship.cool_down == 6
                enemy_increase = 3
                ship.ship_speed = 7
                if window.level == 6:
                    enemy.enemy_velocity = 0.5
                    ship.cool_down = 4
                    ship.ship_speed = 10
            if window.level == 10:
                enemy_increase = 2
                enemy.enemy_boundary = -2000
                ship.ship_speed = 12
            if window.level == 15:
                ship.cool_down = 3
                ship.ship_speed = 15
                enemy_increase = 1
            if window.level == 20:
                ship.cool_down = 1
                ship.ship_speed = 18
                enemy_boundry = -2500
        
            

    # making the game_over and displaying the game over img if lives are 0
            if window.lives <= 0:
                game_over = True
                window.score = 0
                ship.ship_lasers.clear()
                window.game_over()


main_menu()