import pygame
vector = pygame.math.Vector2
keyboard = pygame.key.get_pressed()
class RL_Car():
    def __init__(self, x, y, angle = 0, length = 20):
        self.velocity = vector(0,0)
        self.angle = angle
        self.length = length
        #acceleration is a vector that is = to the change in velocity (derivatives :))
        self.acceleration = 0.0
        self.position = vector(x,y)
    def update_pos(self):
        self.velocity += (self.acceleration)
            if keyboard[pygame.K_LEFT]:
                self.acceleration.x = -0.5
            if keyboard[pygame.K_RIGHT]:
                self.acceleration.x = 0.5
            if keyboard[pygame.K_UP]:
                self.acceleration.y = 0.5
            if keyboard[pygame.K_DOWN]:
                self.acceleration.y = -0.5
    def rotate(self):




