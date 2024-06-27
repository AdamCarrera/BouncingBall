"""
Code for the Ball Object
"""
from dataclasses import dataclass

import pygame
from settings import Boundary, Position, Velocity, RGBColor


@dataclass
class Ball:
    """
    Ball Class
    """
    initial_position: Position
    radius: int
    color: RGBColor
    velocity: Velocity
    render_collider: bool

    def __init__(self, config):
        self.initial_position = config['position']
        self.radius = config['radius']
        self.color = config['color']
        self.velocity = config['velocity']
        self.render_collider = config['render_collider']

        self.collider = pygame.Rect(
            self.initial_position.x - self.radius,
            self.initial_position.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def move(self):
        """
        Update Position and check for collisions

        If the ball touches the top or bottom boundaries, change the y-velocity
        If the ball touches the left or right boundaries, change the x-velocity

        """

        # # Update Position Tuple
        # next_pos = Position(
        #     self.initial_position.x + self.velocity.x,
        #     self.initial_position.y + self.velocity.y
        # )
        # self.initial_position = next_pos

        # Move the collider
        self.collider = self.collider.move(self.velocity.x, self.velocity.y)

        # Check boundary collisions top and bottom
        if (
            self.collider.clipline(Boundary.TOP.value)
            or self.collider.clipline(Boundary.BOTTOM.value)
        ):
            self.color = RGBColor.random()

            next_speed = Velocity(self.velocity.x, self.velocity.y * -1)
            self.velocity = next_speed

        # Check boundary collisions left and right
        if (
            self.collider.clipline(Boundary.LEFT.value)
            or self.collider.clipline(Boundary.RIGHT.value)
        ):
            self.color = RGBColor.random()

            next_speed = Velocity(self.velocity.x * -1, self.velocity.y)
            self.velocity = next_speed

    def draw(self, screen: pygame.Surface):
        """
        Draw the circle object
        """
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.collider.centerx), int(self.collider.centery)),
            self.radius
        )

        if self.render_collider:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                self.collider,
                1
            )
