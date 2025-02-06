import pygame
#Initialize pygame
pygame.init()


#Window setup (dimension and name)
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong pvp")
#Frames per second
FPS = 60
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#Paddle characteristics
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
#Ball characteristics
BALL_RADIUS = 7
#Score font
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
#Score goal
WINNING_SCORE = 10


#Class for paddle
class Paddle:
    #Class attributes
    COLOR = WHITE
    VEL = 4
    #Instance methods
    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
    def move_up(self):
        if self.y - self.VEL >= 0:
            self.y -= self.VEL
    def move_down(self):
        if self.y + self.VEL + self.height <= HEIGHT:
            self.y += self.VEL
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

#Class for ball
class Ball:
    #Class Attributes
    COLOR = WHITE
    MAX_VEL = 5
    #Instance methods
    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = self.MAX_VEL
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


#Rendering game objects
def draw(win, paddles, ball, left_score, right_score):
    #Window render
    win.fill(BLACK)
    #Scores render
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH *3//4 - right_score_text.get_width()//2, 20))
    #Paddles render
    for paddle in paddles:
        paddle.draw(win)
    #Dotted line render
    for i in range(10, HEIGHT, HEIGHT//20):
        if i %2 ==1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))
    #Ball render
    ball.draw(win)
    #Updates screen
    pygame.display.update()

#Handles collisions
def handle_collision(ball, left_paddle, right_paddle):
    #Handles collisions with top and bottom of window
    if ball.y + ball.radius >= HEIGHT or ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    #Handles collision for left paddle
    if ball.x_vel < 0:
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1
                #Changes vel of ball
                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                ball.y_vel = -1 * (difference_in_y / reduction_factor)
    #Handles collision for right paddle
    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                #Changes vel of ball
                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                ball.y_vel = -1 * (difference_in_y / reduction_factor)

#Movement for paddles
def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.move_up()
    if keys[pygame.K_s]:
        left_paddle.move_down()
    if keys[pygame.K_UP]:
        right_paddle.move_up()
    if keys[pygame.K_DOWN]:
        right_paddle.move_down()

#Main function of the game
def main():
    run = True
    clock = pygame.time.Clock()
    #Paddle/ball creation and positioning
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)
    #Initialize scores
    left_score = 0
    right_score = 0
    #Game loop
    while run:
        clock.tick(FPS)
        #Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #Handles a pressed key
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        #Update game state
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)
        #Check for scoring
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()
        #Check for win condition
        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left player wins!"
        if right_score >= WINNING_SCORE:
            won = True
            win_text = "Right player wins!"
        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0
        #Draw game objects
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

    pygame.quit()



if __name__ == "__main__":
    main()