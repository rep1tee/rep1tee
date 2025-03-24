import pygame

class GameObject:
    def __init__(self, image_path, x, y, width, height):
        # Если изображение не найдено, создаем пустой Surface
        try:
            self.image = pygame.image.load(image_path)
        except FileNotFoundError:
            self.image = pygame.Surface((width, height))
            self.image.fill((255, 0, 0))  # Заливаем красным цветом для видимости
        self.rect = self.image.get_rect(topleft=(x, y))
        self.width = width
        self.height = height

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Player(GameObject):
    def __init__(self, image_path, x, y, speed):
        super().__init__(image_path, x, y, 32, 32)
        self.speed = speed

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Enemy(GameObject):
    def __init__(self, image_path, x, y, speed):
        super().__init__(image_path, x, y, 32, 32)
        self.speed = speed

    def move_towards_player(self, player_pos):
        if self.rect.x < player_pos[0]:
            self.rect.x += self.speed
        elif self.rect.x > player_pos[0]:
            self.rect.x -= self.speed
        if self.rect.y < player_pos[1]:
            self.rect.y += self.speed
        elif self.rect.y > player_pos[1]:
            self.rect.y -= self.speed

class Bonus(GameObject):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y, 16, 16)

class Obstacle(GameObject):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y, 32, 32)

class MovingObstacle(GameObject):
    def __init__(self, image_path, x, y, speed):
        super().__init__(image_path, x, y, 32, 32)
        self.speed = speed

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = 0