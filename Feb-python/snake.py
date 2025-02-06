import pygame
import sys
import random

vec2 = pygame.math.Vector2

class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pygame.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.get_random_position()
        self.direction = vec2(self.size, 0)
        self.step_delay = 100
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}

    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.directions[pygame.K_w]:
                self.direction = vec2(0, -self.size)
                self.directions = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_s and self.directions[pygame.K_s]:
                self.direction = vec2(0, self.size)
                self.directions = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_a and self.directions[pygame.K_a]:
                self.direction = vec2(-self.size, 0)
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
            if event.key == pygame.K_d and self.directions[pygame.K_d]:
                self.direction = vec2(self.size, 0)
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}

    def delta_time(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def get_random_position(self):
        return [random.randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)] * 2
    
    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.new_game()
        if self.rect.top <0 or self.rect.bottom >self.game.WINDOW_SIZE:
            self.game.new_game()

    def check_food(self):
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()
            self.length += 1

    def check_selfeating(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]

    def update(self):
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.move()

    def draw(self):
        [pygame.draw.rect(self.game.screen, "green", segment) for segment in self.segments]

class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pygame.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.game.snake.get_random_position()
    def draw(self):
        pygame.draw.rect(self.game.screen, "red", self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW_SIZE = 800
        self.TILE_SIZE = 50
        self.screen = pygame.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pygame.time.Clock()
        self.new_game()

    def draw_grid(self):
        [pygame.draw.line(self.screen, [50]*3, (x, 0), (x, self.WINDOW_SIZE))
         for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        [pygame.draw.line(self.screen, [50]*3, (0, y), (self.WINDOW_SIZE, y))
         for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        
    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)

    def update(self):
        self.snake.update()
        pygame.display.flip()
        self.clock.tick(60)

    def draw(self):
        self.screen.fill("black")
        self.draw_grid()
        self.food.draw()
        self.snake.draw()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            self.snake.control(event)

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()



if __name__ == "__main__":
    game = Game()
    game.run()
