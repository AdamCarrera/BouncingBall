"""
Constants for ball game
"""


from enum import Enum
from typing import NamedTuple

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


BACKGROUND_COLOR = (0, 0, 0)

# Configuration for the ball
BALL_CONFIG = {
    'position': Position(WIDTH // 2, HEIGHT // 2),
    'radius': 50,
    'color': (255, 0, 0),
    'velocity': Velocity(7, 4),
    'render_collider': True
}
