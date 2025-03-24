import pygame
import sys


class two:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.player = pygame.Rect(50, 50, 50, 50)
        self.exit = pygame.Rect(screen.get_width() - 100, screen.get_height() - 100, 50, 50)
        self.walls = [
            pygame.Rect(150, 150, 200, 20),
            pygame.Rect(350, 150, 20, 200),
            pygame.Rect(150, 250, 200, 20),
            # Добавьте дополнительные стены здесь
        ]

    def run_level(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_F11:
                        self.settings['fullscreen'] = not self.settings['fullscreen']
                        if self.settings['fullscreen']:
                            self.screen = pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()), pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()), pygame.RESIZABLE)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move_ip(-5, 0)
            if keys[pygame.K_RIGHT]:
                self.player.move_ip(5, 0)
            if keys[pygame.K_UP]:
                self.player.move_ip(0, -5)
            if keys[pygame.K_DOWN]:
                self.player.move_ip(0, 5)

            for wall in self.walls:
                if self.player.colliderect(wall):
                    if keys[pygame.K_LEFT]:
                        self.player.move_ip(5, 0)
                    if keys[pygame.K_RIGHT]:
                        self.player.move_ip(-5, 0)
                    if keys[pygame.K_UP]:
                        self.player.move_ip(0, 5)
                    if keys[pygame.K_DOWN]:
                        self.player.move_ip(0, -5)

            if self.player.colliderect(self.exit):
                running = False

            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (0, 255, 0), self.player)
            pygame.draw.rect(self.screen, (255, 0, 0), self.exit)

            for wall in self.walls:
                pygame.draw.rect(self.screen, (255, 255, 255), wall)

            pygame.display.flip()
            clock.tick(60)