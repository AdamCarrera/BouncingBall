"""
Constants for ball game
"""


from enum import Enum
from typing import NamedTuple
import random
import pygame

# Screen dimensions
WIDTH, HEIGHT = 800, 600
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
        x_component = random.randint(3, 5) * random.choice([-1, 1])
        y_component = random.randint(3, 5) * random.choice([-1, 1])

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
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
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


def create_config(index: int) -> dict:
    """
    return a config dictionary for the ball class
    offset the position of the ball by index * 50
    so that they don't overlap
    """

    radius = 20
    position = Position(
        (index + 1) * radius * 2,
        (index + 1) * radius * 2
    )

    return {
        'position': position,
        'radius': radius,
        'color': RGBColor.random(),
        'velocity': Velocity.random(),
        'render_collider': False
    }


# Amount of balls in the simulation
N_BALLS = 20
