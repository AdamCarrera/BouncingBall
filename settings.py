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


class Velocity(NamedTuple):
    """
    NamedTuple for velocity with x and y components
    """
    x: int
    y: int

    @staticmethod
    def random() -> 'Velocity':
        """
        return a velocity object with randomized components
        """
        return Velocity(random.randint(5, 10), random.randint(5, 10))


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

# Configuration for the ball
BALL_CONFIG = {
    'position': Position(WIDTH // 2, HEIGHT // 2),
    'radius': 50,
    'color': RGBColor.random(),
    'velocity': Velocity.random(),
    'render_collider': False
}

N_BALLS = 5
