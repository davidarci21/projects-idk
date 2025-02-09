import pygame
import random
import numpy as np
pygame.init()

#Screen set up
WIDTH, HEIGHT = 380 ,760
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
#Frames
FPS = 30
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
RED = (255, 0, 0)
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
#Font
FONT = pygame.font.SysFont("comicsans", 40)


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
    def move_up(self):
        self.y -= 1
    def move_down(self):
        self.y += 1
    def move_left(self):
        self.x -= 1
    def move_right(self):
        self.x +=1
    def rotation(self, grid):
        original_shape = self.shape
        original_x = self.x
        original_y = self.y
        #Rotates matrix
        matrix = np.array(self.shape)
        rotated = np.rot90(matrix, k=1)
        self.shape = rotated.tolist()
        #Checks for collision after rotation
        if handle_collision(block, grid):
            self.x += 1
            if handle_collision(block, grid):
                self.x -= 2
                if handle_collision(block, grid):
                    self.x += 1
                    self.shape = original_shape

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

#Handles collision with grid and other blocks
def handle_collision(block, grid):
    for row in range(len(block.shape)):
        for col in range(len(block.shape[row])):
            if block.shape[row][col]:
                x = block.x + col
                y = block.y + row
                if x < 0 or x >= len(grid[0]) or y >= len(grid):
                    return True
                if y >= 0 and grid[y][x]:
                    return True             
    return False

#Handles block movement
def handle_block_movement(keys, block, grid):
    if keys[pygame.K_DOWN]:
        block.move_down()
        if handle_collision(block, grid):
            block.move_up()
    if keys[pygame.K_UP]:
        original_shape = block.shape
        block.rotation(block, grid)
        if handle_collision(block, grid):
            block.shape = original_shape
    if keys[pygame.K_LEFT]:
        block.move_left()
        if handle_collision(block, grid):
            block.move_right()         
    if keys[pygame.K_RIGHT]:
        block.move_right()
        if handle_collision(block, grid):
            block.move_left()

#Checks and locks a block
def lock_block(block, grid):
    for row in range(len(block.shape)):
        for col in range (len(block.shape[row])):
            if block.shape[row][col]:
                x = block.x + col
                y = block.y + row
                if y >= 0:
                    grid[y][x] = 1

#Clear full rows
def clear_rows(grid):
    rows_to_clear = []
    for row in range(len(grid)):
        if all (grid[row]):
            rows_to_clear.append(row)
    for row in rows_to_clear:
        del grid[row]
        grid.insert(0, [0 for _ in range(GRID_WIDTH)])


#Main function of game
def main():
    run = True
    game_over = False
    clock = pygame.time.Clock()
    #Block instance/creation and positioning
    block = Block()
    move_down_counter = 0
    move_down_delay = 15
    
    #Main loop
    while run:
        clock.tick(FPS)
        #Checks for closing tab
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not game_over:
        #Handles a pressed key
            keys = pygame.key.get_pressed()
            handle_block_movement(keys, block, grid)
            #Moves blocks down automatically with a delay
            move_down_counter += 1
            if move_down_counter >= move_down_delay:
                move_down_counter = 0
                block.move_down()
                #Checks for collisions, locks the block, deletes full rows, and spawns a new block
                if handle_collision(block, grid):
                    block.move_up()
                    lock_block(block, grid)
                    clear_rows(grid)
                    block = Block()
                    if handle_collision(block, grid):
                        game_over = True
        #Draw game objects
        draw(WIN, grid, block)
        #Checks for overlaping of blocks and displays "Game Over"
        if game_over:
            text = FONT.render("Game Over", 1, RED)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            run = False

    pygame.quit()
                    


if __name__ == "__main__":
    main()