import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Always destroy the current asteroid
        self.kill()

        # If already at minimum size, don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle between 20° and 50°
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current one
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Compute the new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new smaller asteroids at the same position
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2
