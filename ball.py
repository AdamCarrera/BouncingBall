"""
Code for the Ball Object
"""
from dataclasses import dataclass

from typing import Union
from math import sqrt
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

    def move(self) -> None:
        """
        Update Position and check for collisions

        If the ball touches the top or bottom boundaries, change the y-velocity
        If the ball touches the left or right boundaries, change the x-velocity

        """

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

    def draw(self, screen: pygame.Surface) -> None:
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


def check_collision(ball_list: list[Ball]) -> Union[tuple[Ball, Ball], tuple]:
    """
    given a list of balls, check if a ball is colliding with any of the others
    """
    for current_ball in ball_list:
        other_balls = [ball for ball in ball_list
                       if ball.collider != current_ball.collider]

        for test_ball in other_balls:
            if current_ball.collider.colliderect(test_ball.collider):
                return (current_ball, test_ball)

    return ()


def calculate_collision(b1: Ball, b2: Ball):
    """
    Given a pair of colliding balls, calculate the new velocities for each
    """
    pos1, speed1 = b1.collider.center, b1.velocity
    pos2, speed2 = b2.collider.center, b2.velocity

    collision_normal = (pos1[0] - pos2[0], pos1[1] - pos2[1])
    distance = sqrt(collision_normal[0]**2 + collision_normal[1]**2)
    collision_normal = (
        collision_normal[0] / distance,
        collision_normal[1] / distance
    )
    # collision_normal = map(lambda x: x / distance, collision_normal)

    relative_velocity = (speed1.x - speed2.x, speed1.y - speed2.y)
    relative_speed = relative_velocity[0] * collision_normal[0] \
        + relative_velocity[1] * collision_normal[1]

    new_speed1 = (
        speed1.x - relative_speed * collision_normal[0],
        speed1.y - relative_speed * collision_normal[1]
    )
    new_speed2 = (
        speed2.x + relative_speed * collision_normal[0],
        speed2.y + relative_speed * collision_normal[1]
    )

    b1.velocity = Velocity(new_speed1[0], new_speed1[1])
    b1.color = RGBColor.random()

    b2.velocity = Velocity(new_speed2[0], new_speed2[1])
    b2.color = RGBColor.random()
