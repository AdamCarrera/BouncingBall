"""
Code for the Ball Object
"""
from dataclasses import dataclass

from typing import Optional
from math import sqrt
import pygame
from settings import (
    Position,
    Velocity,
    RGBColor,
    WIDTH,
    HEIGHT
)

BallPair = tuple['Ball', 'Ball']


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

    def __repr__(self) -> str:
        return f"Position: {self.collider.center}"

    def move(self) -> None:
        """
        Update Position and check for collisions
        using the boundary of the collider
        """

        self.collider = self.collider.move(self.velocity.x, self.velocity.y)

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


def check_collision(ball: Ball, ball_list: list[Ball]) -> Optional[BallPair]:
    """
    Given a list of balls, check if the given ball
    is colliding with any of the others
    """
    for other_ball in ball_list:
        if ball == other_ball:
            continue

        dx = ball.collider.center[0] - other_ball.collider.center[0]
        dy = ball.collider.center[1] - other_ball.collider.center[1]
        distance = sqrt(dx**2 + dy**2)

        if distance < ball.radius + other_ball.radius:
            return (ball, other_ball)
    return None


def check_boundary_collision(ball: Ball) -> bool:
    """
    Check if the ball is colliding with the boundaries of the screen
    """
    next_position = ball.collider.move(ball.velocity.x, ball.velocity.y)

    # Check boundary collisions top and bottom
    if next_position.top < 0:
        ball.collider.centery = 0 + ball.radius
        ball.velocity = Velocity(ball.velocity.x, ball.velocity.y * -1)
        ball.color = RGBColor.random()
        return True

    if next_position.bottom > HEIGHT:
        ball.collider.centery = HEIGHT - ball.radius
        ball.velocity = Velocity(ball.velocity.x, ball.velocity.y * -1)
        ball.color = RGBColor.random()
        return True

    # Check boundary collisions left and right
    if next_position.left < 0:
        ball.collider.centerx = 0 + ball.radius
        ball.velocity = Velocity(ball.velocity.x * -1, ball.velocity.y)
        ball.color = RGBColor.random()
        return True

    if next_position.right > WIDTH:
        ball.collider.centerx = WIDTH - ball.radius
        ball.velocity = Velocity(ball.velocity.x * -1, ball.velocity.y)
        ball.color = RGBColor.random()
        return True

    return False


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

    relative_velocity = (speed1.x - speed2.x, speed1.y - speed2.y)
    relative_speed = relative_velocity[0] * collision_normal[0] \
        + relative_velocity[1] * collision_normal[1]

    # if the relative speed is negative
    # then the balls are moving away from each other
    # and we don't need to do anything
    if relative_speed > 0:
        return

    new_speed1 = Velocity(
        speed1.x - relative_speed * collision_normal[0],
        speed1.y - relative_speed * collision_normal[1]
    )
    new_speed2 = Velocity(
        speed2.x + relative_speed * collision_normal[0],
        speed2.y + relative_speed * collision_normal[1]
    )

    b1.velocity = new_speed1
    b1.color = RGBColor.random()

    b2.velocity = new_speed2
    b2.color = RGBColor.random()

    next_distance = sqrt(
        (pos1[0] + new_speed1.x - pos2[0] - new_speed2.x)**2
        + (pos1[1] + new_speed1.y - pos2[1] - new_speed2.y)**2
    )

    # Overlap Handling
    if next_distance < b1.radius + b2.radius:

        overlap = b1.radius + b2.radius - distance

        b1.collider = b1.collider.move(
            overlap * collision_normal[0],
            overlap * collision_normal[1]
        )
        b2.collider = b2.collider.move(
            -overlap * collision_normal[0],
            -overlap * collision_normal[1]
        )
