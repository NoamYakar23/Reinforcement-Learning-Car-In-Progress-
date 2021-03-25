import pygame
vector = pygame.math.Vector2
events = pygame.event.get()
class RL_Car():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.velocity = vector(0,0)
        self.angle = 0
        self.acceleration = vector(0,0)
    def update_pos(self):
        self.acceleration = vector(0,0)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.acceleration.x = -0.5
                if event.key == pygame.K_RIGHT:
                    self.acceleration.x = 0.5
                if event.key == pygame.K_UP:
                    self.acceleration.y = 0.5
                if event.key == pygame.K_DOWN:
                    self.acceleration.y = -0.5



