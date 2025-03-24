import pygame
import sys
from pygame.locals import *

class MazeLevel:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.player = pygame.Rect(50, 50, 50, 50)
        self.exit = pygame.Rect(screen.get_width() - 100, screen.get_height() - 100, 50, 50)

        self.walls = [
            pygame.Rect(100, 100, 200, 20),
            pygame.Rect(300, 100, 20, 200),
            pygame.Rect(100, 200, 200, 20),
        ]
        self.bonuses = [
            pygame.Rect(150, 150, 20, 20),
            pygame.Rect(350, 250, 20, 20),
        ]
        self.enemies = [
            pygame.Rect(250, 250, 50, 50),
        ]

    def run_level(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_F11:
                        self.settings['fullscreen'] = not self.settings['fullscreen']
                        if self.settings['fullscreen']:
                            self.screen = pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()), pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()), pygame.RESIZABLE)

            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.player.move_ip(-5, 0)
            if keys[K_RIGHT]:
                self.player.move_ip(5, 0)
            if keys[K_UP]:
                self.player.move_ip(0, -5)
            if keys[K_DOWN]:
                self.player.move_ip(0, 5)

            for wall in self.walls:
                if self.player.colliderect(wall):
                    if keys[K_LEFT]:
                        self.player.move_ip(5, 0)
                    if keys[K_RIGHT]:
                        self.player.move_ip(-5, 0)
                    if keys[K_UP]:
                        self.player.move_ip(0, 5)
                    if keys[K_DOWN]:
                        self.player.move_ip(0, -5)

            for bonus in self.bonuses:
                if self.player.colliderect(bonus):
                    self.bonuses.remove(bonus)
                    # Добавьте логику для получения бонуса

            for enemy in self.enemies:
                if self.player.colliderect(enemy):
                    running = False
                    # Добавьте логику для столкновения с врагом

            if self.player.colliderect(self.exit):
                running = False

            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (0, 255, 0), self.player)
            pygame.draw.rect(self.screen, (255, 0, 0), self.exit)

            for wall in self.walls:
                pygame.draw.rect(self.screen, (255, 255, 255), wall)

            for bonus in self.bonuses:
                pygame.draw.rect(self.screen, (0, 0, 255), bonus)

            for enemy in self.enemies:
                pygame.draw.rect(self.screen, (255, 0, 0), enemy)

            pygame.display.flip()
            clock.tick(60)