import pygame
class Game():
    def __init__(self, width = 1280, height = 720, framerate = 60):
        pygame.init()
        self.width = width
        self.height = height
        #framerate
        self.framerate = framerate
        self.screen = pygame.display.set_mode(width, height)

        self.exit_bool = False
    def run(self):
        while not self.exit_bool:
            for event in pygame.event.get():
                if event.type == pygame.EXIT()
                    self.exit_bool = True

            keyboard = pygame.key.get_pressed()


