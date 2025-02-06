import pygame
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

#Class for paddle
class Paddle:
    #Class attributes
    COLOR = WHITE
    VEL = 4
    #Instance methods
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
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
        

#Rendering game objects
def draw(win, paddles):
    #Window render
    win.fill(BLACK)
    #Paddles render
    for paddle in paddles:
        paddle.draw(win)
    #Dotted line render
    for i in range(10, HEIGHT, HEIGHT//20):
        if i %2 ==1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    pygame.display.update()

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
    #Paddle creation and positioning
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    #Game loop
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle])
        #Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #Handles a pressed key
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit()



if __name__ == "__main__":
    main()