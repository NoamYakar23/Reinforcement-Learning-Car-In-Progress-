import pygame

from RL_Car import RL_Car

pygame.init()
class Game:
    def __init__(self, width = 1280, height = 720, framerate = 60):
        self.width = width
        self.height = height
        #framerate
        self.framerate = framerate
        self.screen = pygame.display.set_mode(width, height)
        self.clock = pygame.time.Clock()

        self.exit_bool = False
    def run(self):
        RL_Car(0,0)
        car = pygame.image.load('car.png')
        while not self.exit_bool:
            dt = self.clock.get_time() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    self.exit_bool = True

            keyboard = pygame.key.get_pressed()

            if keyboard[pygame.K_UP]:
                if RL_Car.velocity.x < 0:
                    RL_Car.acceleration = RL_Car.natural_deceleration
                else:
                    RL_Car.acceleration += 1 * dt

            elif keyboard[pygame.K_DOWN]:
                if RL_Car.velocity.x > 0:
                    RL_Car.acceleration = -RL_Car.natural_deceleration
                else:
                    RL_Car.acceleration -= 1 * dt
            elif keyboard[pygame.K_SPACE]:

            else:




            if keyboard[pygame.K_RIGHT]:
                RL_Car.steering -= 30 * dt
            elif keyboard[pygame.K_LEFT]:
                RL_Car.steering += 30 * dt
            else:
                RL_Car.steering_value = 0
            RL_Car.steering_value = max(-RL_Car.steering_value, min(RL_Car.steering_value,RL_Car.max_steering_angle))



if __name__ == '__main__':
    game = Game()
    game.run()




