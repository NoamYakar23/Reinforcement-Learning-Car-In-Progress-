import pygame
from kivy.vector import Vector
from math import *

vector = pygame.math.Vector2
keyboard = pygame.key.get_pressed()

class RL_Car():
    def __init__(self, x, y, angle = 0, length = 20):
        self.angle = angle
        self.length = length
        #acceleration is a vector that is = to the change in velocity (derivatives :))
        self.acceleration = 0.0
        self.position = vector(x,y)
        self.x = x
        self.y = y
        self.steering_value = 0.0
        self.clock = pygame.time.Clock()
        self.max_steering_angle = 30

    def update_position(self):
        dt = self.clock.get_time() / 1000
        self.velocity += vector(self.acceleration * dt, 0)

        if self.steering_value > 0:
            angle_of_rotation = self.length / sin(radians(self.max_steering_angle))
            angular_speed = self.velocity.x / angle_of_rotation
        else:
            angular_speed = 0.0
        self.position = self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_speed) * dt
        
        if keyboard[pygame.K_LEFT]:
            self.acceleration.x = -0.5
        if keyboard[pygame.K_RIGHT]:
            self.acceleration.x = 0.5
        if keyboard[pygame.K_UP]:
            self.acceleration.y = 0.5
        if keyboard[pygame.K_DOWN]:
            self.acceleration.y = -0.5






