import pygame
pygame.init()

#Screen set up
WIDTH, HEIGHT = 400 ,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
#Frames
FPS = 60
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#Grid
GRID_WIDTH, GRID_HEIGHT = 10, 20
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#Blocks
blocks = {
    "T": [[1, 1, 1], [0, 1, 0]], 
    "O": [[1, 1], [1, 1]], 
    "I": [[1, 1, 1, 1]], 
    "S": [[0, 1, 1], [1, 1, 0]], 
    "Z": [[1, 1, 0], [0, 1, 1]], 
    "L": [[1, 0], [1, 0], [1, 1]], 
    "J": [[0, 1], [0, 1], [1,1]]
}
print(blocks)
#Classes
class Block:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y
    def move_down(self):
        pass
    def move_sides(self):
        pass
    def rotation(self):
        pass






#Functions 
def draw(win, grid, tetraminos):
    pass
def handle_collision():
    pass
def handle_movement():
    pass




#Main function of game
def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False

        #Handle user input.
        # Move the tetromino down.
        #Check for collisions.
        #Lock the tetromino if it can't move further.
        #Clear completed lines.
        #Spawn a new tetromino.
        #draw(WIN, )
        #print(T)

    pygame.quit()
                    

















if __name__ == "__main__":
    main()