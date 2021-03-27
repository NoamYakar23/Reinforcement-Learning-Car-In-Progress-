import os
import pygame
from math import sin, radians, degrees, copysign

from Car import Car

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Reinforcement Learning Parking")
        width = 1280
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        car_image = pygame.image.load(image_path)
        build = Car(0, 0)


        while not self.exit:
            dt = self.clock.get_time() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                if build.velocity.x < 0:
                    build.acceleration = build.brake_deceleration
                else:
                    build.acceleration += 1 * dt
            elif keys[pygame.K_DOWN]:
                if build.velocity.x > 0:
                    build.acceleration = -build.brake_deceleration
                else:
                    build.acceleration -= 1 * dt
            elif keys[pygame.K_SPACE]:
                if abs(build.velocity.x) > dt * build.brake_deceleration:
                    build.acceleration = -copysign(build.brake_deceleration, build.velocity.x)
                else:
                    build.acceleration = -build.velocity.x / dt
            else:
                if abs(build.velocity.x) > dt * build.free_deceleration:
                    build.acceleration = -copysign(build.free_deceleration, build.velocity.x)
                else:
                    if dt != 0:
                        build.acceleration = -build.velocity.x / dt
            build.acceleration = max(-build.max_acceleration, min(build.acceleration, build.max_acceleration))

            if keys[pygame.K_RIGHT]:
                build.steering -= 30 * dt
            elif keys[pygame.K_LEFT]:
                build.steering += 30 * dt
            else:
                build.steering = 0
            build.steering = max(-build.max_steering, min(build.steering, build.max_steering))
            build.update(dt)

            # Drawing
            self.screen.fill((0, 0, 0))
            rotated = pygame.transform.rotate(car_image, build.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, build.position * 32 - (rect.width / 2, rect.height / 2))
            pygame.display.flip()

            self.clock.tick(self.ticks)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
