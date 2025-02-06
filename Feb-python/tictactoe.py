import sys, random, pygame

WIN_SIZE = 800

class TicTacToe:
    def __init__(self, game):
        pass
    def run(self):
        pass

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIN_SIZE] * 2)
        self.clock = pygame.time.Clock()
        self.tic_tac_toe = TicTacToe(self)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()