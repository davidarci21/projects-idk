import pygame
import sys
import random
#Initialize Pygame
pygame.init()


#Screen dimensions
screen_width = 1280
screen_height = 800
#Initialize screen and clock
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()
#Game objects
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (screen_width/2, screen_height/2)
cpu = pygame.Rect(0, 0, 20, 100)
cpu.centery = (screen_height/2)
player = pygame.Rect(0, 0, 20, 100)
player.midright = (screen_width, screen_height/2)
#Game variables
ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
cpu_speed = 6
cpu_points, player_points = 0, 0
#Font for score
score_font = pygame.font.Font(None, 100)


#Resets position of ball
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_y *= random.choice([-1,1])
    ball_speed_x *= random.choice([-1,1])

#Updates score and calls reset_ball
def point_won(winner):
    global cpu_points, player_points
    if winner == "cpu":
        cpu_points += 1
    if winner == "player":
        player_points +=1
    reset_ball()

#Updates ball position and handles collisions
def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    #Collision with top and bottom wall
    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1
    #Ball goes out of window
    if ball.right >=screen_width:
        point_won("cpu")
    if ball.left <= 0:
        point_won("player")
    #Collision with paddle
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1

#Update player's paddle position
def animate_player():
    player.y += player_speed
    #Handles paddle out of window
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

#Updates cpu's paddle position based on ball position
def animate_cpu():
    global cpu_speed
    cpu.y += cpu_speed
    #Paddle follows ball 
    if ball.centery <= cpu.centery:
        cpu_speed = -6
    if ball.centery >= cpu.centery:
        cpu_speed = 6
    #Handles paddle out of window
    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= screen_height:
        cpu.bottom = screen_height

#Main game loop
while True:
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed = 0
    #Change position of objects
    animate_ball()
    animate_player()
    animate_cpu()
    #Draw game objects
    screen.fill("black")
    pygame.draw.aaline(screen, "white", (screen_width/2, 0), (screen_width/2, screen_height)) #line in the middle
    pygame.draw.ellipse(screen, "white", ball) #ball
    pygame.draw.rect(screen, "white", cpu) #cpu paddle
    pygame.draw.rect(screen, "white", player) #player paddle
    #Draw scores
    cpu_score_surface = score_font.render(str(cpu_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")
    screen.blit(cpu_score_surface, (screen_width/4, 20))
    screen.blit(player_score_surface, (3*screen_width/4, 20))
    #Update display
    pygame.display.update()
    clock.tick(60)
