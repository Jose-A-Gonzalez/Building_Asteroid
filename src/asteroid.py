from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen : "Surface"):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        first_asteroid_mov = self.velocity.rotate(random_angle)
        second_asteroid_mov = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_ast = Asteroid(self.position.x,self.position.y,new_radius)
        second_ast = Asteroid(self.position.x,self.position.y,new_radius)
        first_ast.velocity = first_asteroid_mov * 1.2
        second_ast.velocity = second_asteroid_mov * 1.2





