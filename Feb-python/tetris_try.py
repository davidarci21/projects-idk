import pygame
import random
pygame.init()

#Screen set up
WIDTH, HEIGHT = 380 ,760
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
#Frames
FPS = 30
MOVE_DOWN_DELAY = 15
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
#Grid
GRID_WIDTH, GRID_HEIGHT = 10, 20
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#Cell
CELL_SIZE = WIDTH//GRID_WIDTH
#Blocks
BLOCKS = {
    "T": {"shape": [[1, 1, 1], [0, 1, 0]], "color": PURPLE}, 
    "O": {"shape": [[1, 1], [1, 1]], "color": YELLOW},
    "I": {"shape": [[1, 1, 1, 1]], "color": CYAN},
    "S": {"shape": [[0, 1, 1], [1, 1, 0]], "color": GREEN},
    "Z": {"shape": [[1, 1, 0], [0, 1, 1]], "color": RED},
    "L": {"shape": [[1, 0], [1, 0], [1, 1]], "color": ORANGE},
    "J": {"shape": [[0, 1], [0, 1], [1, 1]], "color": BLUE}
}
#Font
FONT = pygame.font.SysFont("comicsans", 40)


#Classes
class Block:
    def __init__(self):
        self.type = random.choice(list(BLOCKS.keys()))
        self.shape = BLOCKS[self.type]["shape"]
        self.color = BLOCKS[self.type]["color"]
        self.x = 3
        self.y = 0
    #Draws the instance based on its shape
    def draw(self, win):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]:
                    x = (self.x + col) * CELL_SIZE
                    y = (self.y + row) * CELL_SIZE
                    pygame.draw.rect(win, self.color, (x, y, CELL_SIZE, CELL_SIZE))
    #Movement methods
    def move_down(self, grid):
        self.y += 1
        if handle_collision(self, grid):
            self.y -= 1
            return False
        return True
    def move_left(self):
        self.x -= 1
    def move_right(self):
        self.x +=1
    #Rotation method
    def rotate(self, grid):
        original_shape = self.shape
        original_x = self.x
        original_y = self.y
        #Rotates matrix
        rotated = list(zip(*self.shape[::-1]))
        self.shape = [list(row) for row in rotated]
        #Checks for collision after rotation
        if handle_collision(self, grid):
            self.x += 1
            if handle_collision(self, grid):
                self.x -= 2
                if handle_collision(self, grid):
                    self.y -= 1
                    if handle_collision(self, grid):
                        self.shape = original_shape
                        self.x = original_x
                        self.y = original_y

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
            if grid[row][col] != 0:
                pygame.draw.rect(win, grid[row][col], (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(win, GRAY, (x, y, CELL_SIZE, CELL_SIZE), 1)
        #Renders gray lines for better visualization of grid
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
def handle_movement(block, grid, keys):
    #Down arrow pressed
    if keys[pygame.K_DOWN]:
        block.move_down(grid)
    #Left arrow pressed
    if keys[pygame.K_LEFT]:
        block.move_left()
        if handle_collision(block, grid):
            block.move_right()
    #Right arrow pressed        
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
                    grid[y][x] = block.color

#Clear full rows
def clear_rows(grid):
    #Creates a list
    rows_to_clear = []
    #Checks for full rows and appends to the list
    for row in range(len(grid)):
        if all (grid[row]):
            rows_to_clear.append(row)
    #Deletes rows in list and inserts a new row at the top of the grid
    for row in rows_to_clear:
        del grid[row]
        grid.insert(0, [0 for _ in range(GRID_WIDTH)])

#Main function of game
def main():
    #Initializes game main logic
    run = True
    game_over = False
    clock = pygame.time.Clock()
    #Block instance/creation and positioning
    block = Block()
    move_down_counter = 0
    up_pressed = False
    
    #Main loop
    while run:
        clock.tick(FPS)
        #Stores pressed keys in a variable
        keys = pygame.key.get_pressed()
        #Checks for events
        for event in pygame.event.get():
            #Checks for closing tab
            if event.type == pygame.QUIT:
                run = False
            #Checks for a pressed key
            elif event.type == pygame.KEYDOWN:
                #Checks for type of key pressed
                if event.key == pygame.K_UP and not up_pressed:
                    up_pressed = True
                    #Calls the rotate instance method
                    block.rotate(grid)
            #Checks for a released key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up_pressed = False
        #Calls the handle_movement function for the rest of keys being pressed during the game
        handle_movement(block, grid, keys)
        #Checks for game_over condition
        if not game_over:
            #Moves blocks down automatically with a delay
            move_down_counter += 1
            if move_down_counter >= MOVE_DOWN_DELAY:
                move_down_counter = 0
                #Checks for collisions, locks the block, deletes full rows, and spawns a new block
                if not block.move_down(grid):
                    lock_block(block, grid)
                    clear_rows(grid)
                    block = Block()
                    #Checks for instant collision of a block after being spawned
                    if handle_collision(block, grid):
                        game_over = True
        #Draw game objects
        draw(WIN, grid, block)
        #Checks for overlapping of blocks and displays "Game Over"
        if game_over:
            text = FONT.render("Game Over", 1, RED)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            run = False
    #Closes the window
    pygame.quit()
                    


if __name__ == "__main__":
    main()