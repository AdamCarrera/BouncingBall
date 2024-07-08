"""
Constants for ball game
"""


from enum import Enum
from typing import NamedTuple
import random
import pygame

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2


class Boundary(Enum):
    """
    Enum for boundaries of the screen
    """
    LEFT = ((0, 0), (0, HEIGHT))
    RIGHT = ((WIDTH, 0), (WIDTH, HEIGHT))
    TOP = ((0, 0), (WIDTH, 0))
    BOTTOM = ((0, HEIGHT), (WIDTH, HEIGHT))


class Position(NamedTuple):
    """
    NamedTuple for position with x and y components
    """
    x: int
    y: int

    @staticmethod
    def random() -> 'Position':
        """
        return a position object with randomized components
        """

        x_component = random.randint(50, WIDTH - 300)
        y_component = random.randint(50, HEIGHT - 300)

        return Position(x_component, y_component)


class Velocity(NamedTuple):
    """
    NamedTuple for velocity with x and y components
    """
    x: float
    y: float

    @staticmethod
    def random() -> 'Velocity':
        """
        return a velocity object with randomized components
        """

        # Randomly chose an integer between 5 and 10
        # then randomly change the sign
        x_component = random.randint(5, 6) * random.choice([-1, 1])
        y_component = random.randint(5, 6) * random.choice([-1, 1])

        return Velocity(x_component, y_component)


class RGBColor(pygame.Color):
    """
    Extension of pygame.Color class

    Contains a function for generating a new random color
    """
    r: float
    g: float
    b: float

    @staticmethod
    def random() -> 'RGBColor':
        """
        Return a randomized RGBColor object
        """
        return RGBColor(
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255)
        )


BACKGROUND_COLOR = RGBColor(0, 0, 0)

# example configuration for the ball
BALL_CONFIG = {
    'position': Position.random(),
    'radius': 50,
    'color': RGBColor.random(),
    'velocity': Velocity.random(),
    'render_collider': False
}


def create_random_config(i, j) -> dict:
    """
    return a config dictionary for the ball class
    offset the position of the ball by index * 50
    so that they don't overlap
    """

    radius = 40

    position = Position(
        (j + 1) * (25 + 2 * radius),
        (i + 1) * (25 + 2 * radius)
    )

    return {
        'position': position,
        'radius': radius,
        'color': RGBColor.random(),
        'velocity': Velocity.random(),
        'render_collider': False
    }


def create_test_config(index: int) -> dict:
    """
    return a config dictionary for the ball class
    that can be used for testing and debugging
    """

    vel = 3

    radius = 50
    if index % 2 == 0:
        position = Position((index + 1) * 125, 400)
        velocity = Velocity(vel + 3, 0)
    else:
        position = Position((index + 1) * 125, 401)
        velocity = Velocity(vel, 0)

    return {
        'position': position,
        'radius': radius,
        'color': RGBColor(255, 0, 0),
        'velocity': velocity,
        'render_collider': True
    }


# Amount of balls in the simulation
N_BALLS = 10
N_ROWS = 10
N_COLS = 10
