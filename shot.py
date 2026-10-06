from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame


class Shot(CircleShape):
    def __init__(self, x, y ):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y=y
    containers = (
        # the group that updates objects,
        # the group that draws objects,
        # your new group for shots,
    )
          
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt):
         self.position = self.position + self.velocity * dt
        
        
