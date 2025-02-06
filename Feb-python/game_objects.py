import pygame
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

    def time_delta(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.step_delay:
            return True
        return False

    def get_random_position(self):
        return [random.randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)] * 2
    
    def move(self):
        if self.time_delta():
            self.rect.move_ip(self.direction)

    def update(self):
        self.move()

    def draw(self):
        pygame.draw.rect(self.game.screen, "green", self.rect)

class Food:
    def __init__(self, game):
        pass
    def draw(self):
        pass