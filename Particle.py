import pygame, random


class Particles(pygame.sprite.Sprite):
    # [loc,vel,time]
    def __init__(self, x, y, color,gravity):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.vel = [random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5]
        self.time = random.randint(4, 6)
        self.color = color
        self.gravity = gravity

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.time)

    def update(self):
        self.time -= 0.06
        self.x += self.vel[0] * random.randint(1,6)
        self.y += self.vel[1] * random.randint(1,6)
        self.vel[1] += self.gravity
        if self.time < 0:
            self.kill()
            return False
        return True
