"""
Code for the Ball Object
"""
from dataclasses import dataclass
from typing import Tuple

import pygame
from settings import Boundary, Position, Velocity


@dataclass
class Ball:
    """
    Ball Class
    """
    pos: Position
    radius: int
    color: Tuple[int, int, int]
    velocity: Velocity
    # render_collider: bool

    def __init__(self, config):
        self.pos = config['position']
        self.radius = config['radius']
        self.color = config['color']
        self.velocity = config['velocity']

        self.collider = pygame.Rect(
            self.pos.x - self.radius,
            self.pos.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def move(self):
        """
        Update Position and check for collisions

        If the ball touches the top or bottom boundaries, change the y-velocity
        If the ball touches the left or right boundaries, change the x-velocity

        """

        # Update Position Tuple
        next_pos = Position(
            self.pos.x + self.velocity.x,
            self.pos.y + self.velocity.y
        )
        self.pos = next_pos

        # Move the collider as well
        # Make the collider the main position object?
        self.collider = self.collider.move(self.velocity.x, self.velocity.y)

        if (
            self.collider.clipline(Boundary.TOP.value)
            or self.collider.clipline(Boundary.BOTTOM.value)
        ):
            self.color = (255, 0, 255)

            next_speed = Velocity(self.velocity.x, self.velocity.y * -1)
            self.velocity = next_speed

        if (
            self.collider.clipline(Boundary.LEFT.value)
            or self.collider.clipline(Boundary.RIGHT.value)
        ):
            self.color = (255, 0, 255)

            next_speed = Velocity(self.velocity.x * -1, self.velocity.y)
            self.velocity = next_speed

    def draw(self, screen: pygame.Surface, render_collider=True):
        """
        Draw the circle object
        """
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.pos.x), int(self.pos.y)),
            self.radius
        )

        if render_collider:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                self.collider,
                1
            )
