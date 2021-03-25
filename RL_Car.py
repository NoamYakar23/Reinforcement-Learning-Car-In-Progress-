import pygame
from kivy.vector import Vector
from math import *
#initialize pygame library before using it to manipulate anything in the program
pygame.init()
vector = pygame.math.Vector2
keyboard = pygame.key.get_pressed()
pygame.init()
class RL_Car():
    def __init__(self, x, y, angle = 0, length = 20, max_acceleration = 5):
        self.angle = angle
        self.length = length
        self.velocity = vector(0.0,0.0)
        #acceleration is a vector that is = to the change in velocity (derivatives :))
        self.acceleration = 0.0
        self.position = vector(x,y)
        self.x = x
        self.y = y
        self.steering_value = 0.0
        self.clock = pygame.time.Clock()
        self.max_steering_angle = 30
        self.max_acceleration = max_acceleration
        self.brake_val = 10.0
        self.natural_deceleration = 3.3

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







