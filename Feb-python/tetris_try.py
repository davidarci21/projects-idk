import pygame
import random
pygame.init()

#Screen set up
WIDTH, HEIGHT = 380 ,760
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
#Frames
FPS = 10
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
#Grid
GRID_WIDTH, GRID_HEIGHT = 10, 20
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#Cell
CELL_SIZE = WIDTH//GRID_WIDTH
#Blocks
blocks_dict = {
    "T": [[1, 1, 1], 
          [0, 1, 0]], 
    "O": [[1, 1], 
          [1, 1]], 
    "I": [[1, 1, 1, 1]], 
    "S": [[0, 1, 1], 
          [1, 1, 0]], 
    "Z": [[1, 1, 0], 
          [0, 1, 1]], 
    "L": [[1, 0], 
          [1, 0], 
          [1, 1]], 
    "J": [[0, 1], 
          [0, 1], 
          [1,1]]
}

#Classes
class Block:
    def __init__(self):
        self.shape = random.choice(list(blocks_dict.values()))
        self.x = 3
        self.y = 0
    def draw(self, win):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]:
                    x = (self.x + col) * CELL_SIZE
                    y = (self.y + row) * CELL_SIZE
                    pygame.draw.rect(win, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
    def move_down(self):
        self.y += 1
    def move_left(self):
        self.x -= 1
    def move_right(self):
        self.x +=1
    def rotation(self):
        pass


#Functions
#Rendering objects
def draw(win, grid, block):
    win.fill(BLACK)
    #Draw grid
    render_grid(win, grid)
    #Draw block
    block.draw(win)
    #Update screen
    pygame.display.update()

#Render grid
def render_grid(win, grid):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if grid[row][col] == 0:
                pygame.draw.rect(win, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)
            else:
                pygame.draw.rect(win, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
        for col in range(GRID_WIDTH + 1):
            pygame.draw.line(win, GRAY, (col*CELL_SIZE, 0), (col*CELL_SIZE, HEIGHT))
        for row in range(GRID_HEIGHT + 1):
            pygame.draw.line(win, GRAY, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE))

#Render blocks
def render_blocks():
    pass

#Handles collision with grid and other blocks
def handle_collision():
    pass

#Handles block movement
def handle_block_movement(keys, block):
    if keys[pygame.K_DOWN]:
        block.move_down()
    if keys[pygame.K_UP]:
        block.rotation()
    if keys[pygame.K_LEFT]:
        block.move_left()
    if keys[pygame.K_RIGHT]:
        block.move_right()

#Main function of game
def main():
    run = True
    clock = pygame.time.Clock()
    #Block instance/creation and positioning
    block = Block()
    

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #Handles a pressed key
        keys = pygame.key.get_pressed()
        handle_block_movement(keys, block)
        # Move the tetromino down.
        #Check for collisions.
        #Lock the tetromino if it can't move further.
        #Clear completed lines.
        #Spawn a new tetromino.
        draw(WIN, grid, block)


    pygame.quit()
                    


if __name__ == "__main__":
    main()