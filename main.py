"""
Main file for bouncing ball simulator
"""
import sys
import pygame
from settings import (
    Boundary,
    create_random_config,
    WIDTH,
    HEIGHT,
    BACKGROUND_COLOR,
    N_ROWS,
    N_COLS
)
from ball import (
    Ball,
    check_collision,
    check_boundary_collision,
    calculate_collision,
)


def main():
    """
    Set up and run simulation
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball Simulation")
    clock = pygame.time.Clock()

    balls = [Ball(create_random_config(i, j))
             for i in range(N_ROWS)
             for j in range(N_COLS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for line in Boundary:
            pygame.draw.line(screen, (255, 255, 0), *line.value, 5)

        # go through each ball and check if there's a collision
        # if there is, calculate speeds and directions
        # modify them in place

        for ball in balls:
            wall_collision = check_boundary_collision(ball)
            if wall_collision:
                continue

            collision_pair = check_collision(ball, balls)
            if collision_pair and ball in collision_pair:
                calculate_collision(collision_pair[0], collision_pair[1])
                continue

        # After all of the collisions have been checked
        # move the balls and draw them

        for ball in balls:
            ball.move()
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
