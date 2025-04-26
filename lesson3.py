from tkinter import mainloop
import pygame 
import random

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# Load sounds
shoot_sound = pygame.mixer.Sound("spitonthat thangg.mp3")


#Player
class Player(object):
   def __init__(self):
       self.img = pygame.image.load("chiao gong zhe.png")
       self.img = pygame.transform.scale(self.img, (100, 100))
       self.x = 690
       self.y = 800
       self.x_change = 0
       self.y_change = 0
       self.lives = 3

# Enemy
class Alien(object):
   def __init__(self):
       self.img = pygame.image.load("chicken jockeyy.png")
       self.img = pygame.transform.scale(self.img, (100, 100))
       self.x = 368 # enemy at center, explain
       self.y = 50
       self.x_change = 5
       self.y_change = 10

class Bullet(object):
   def __init__(self):
       self.img = pygame.image.load("super weapon.png")
       self.img = pygame.transform.scale(self.img, (20, 20))
       self.x = 0
       self.y = 496
       self.x_change = 0
       self.y_change = -20
       self.state = "ready"

   def fire_bullet(self, x, y):
        self.state = "fire"
        self.x = x + 40  # Align bullet with the center of the player
        self.y = y

   def move_bullet(self):
        if self.state == "fire":
            self.y += self.y_change
            if self.y <= 0:
                self.y = 496
                self.state = "ready"
    
def draw_player(image, x, y):
    screen.blit(image, (x, y))  
def draw_alien(image, x, y):
    screen.blit(image, (x, y))

# Main Loop
def mainloop():
    running = True
    win_condition = 0
    while running:
        # Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_change = -5
                if event.key == pygame.K_RIGHT:
                    player.x_change = 5
                if event.key == pygame.K_UP:
                    player.y_change = -5
                if event.key == pygame.K_DOWN:
                    player.y_change = 5
                if event.key == pygame.K_SPACE and bullet.state == "ready":
                    bullet.fire_bullet(player.x, player.y)
                    shoot_sound.play()
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    player.x_change = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    player.y_change = 0

        # Update player position
        player.x += player.x_change
        player.y += player.y_change

        # Background
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Draw Player
        draw_player(player.img, player.x, player.y)

        # Move and draw the bullet
        bullet.move_bullet()
        if bullet.state == "fire":
            screen.blit(bullet.img, (bullet.x, bullet.y))

        # Alien Movement and Collision Detection
        for enemy in enemies[:]:  # Iterate over a copy of the list to allow removal
            if enemy.x <= 0:
                enemy.x_change = 5
                enemy.y += enemy.y_change
            elif enemy.x >= 736:
                enemy.x_change = -5
                enemy.y += enemy.y_change

            enemy.x += enemy.x_change

            # Check for collision between bullet and enemy
            enemy_rect = pygame.Rect(enemy.x, enemy.y, 100, 100)  # Enemy size
            bullet_rect = pygame.Rect(bullet.x, bullet.y, 20, 20)  # Bullet size
            if bullet.state == "fire" and enemy_rect.colliderect(bullet_rect):
                bullet.state = "ready"  # Reset bullet
                bullet.y = 496
                enemies.remove(enemy)  # Remove the enemy
                win_condition += 1

            # Draw Alien
            draw_alien(enemy.img, enemy.x, enemy.y)

        # Flip the display
        pygame.display.flip()
        clock.tick(60)

num_of_enemies = 6
enemies = list()
for i in range (num_of_enemies):
    enemy = Alien()
    enemy.x = random.randint(0, 736)
    enemy.y = random.randint(50, 250)
    enemies.append(enemy)

#Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1500, 1070))
pygame.display.set_caption("Hello Pygame!")
clock = pygame.time.Clock()

#background
background = pygame.image.load("thenether.jpg")
clock = pygame.time.Clock()
player = Player()
bullet = Bullet()
mainloop()
pygame.quit()
