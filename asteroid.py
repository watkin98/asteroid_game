from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            one_way = self.velocity.rotate(angle)
            or_another = self.velocity.rotate(-angle)
            new_radii = self.radius - ASTEROID_MIN_RADIUS

            ast1 = Asteroid(0, 0, new_radii)
            ast1.position = pygame.Vector2(self.position.x, self.position.y)
            ast2 = Asteroid(0, 0, new_radii)
            ast2.position = pygame.Vector2(self.position.x, self.position.y)

            ast1.velocity = one_way * 1.2
            ast2.velocity = or_another * 1.2