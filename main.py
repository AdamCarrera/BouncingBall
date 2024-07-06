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
    N_BALLS
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

    balls = [Ball(create_random_config(i)) for i in range(N_BALLS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for line in Boundary:
            pygame.draw.line(screen, (255, 255, 0), *line.value, 5)

        # go through each ball and check if there's a collision
        # if there is, calculate speed then move
        # if there isnt, move
        for i, ball in enumerate(balls):

            wall_collision = check_boundary_collision(ball)
            if wall_collision:
                continue

            collision_pair = check_collision(balls)

            if collision_pair:

                calculate_collision(collision_pair[0], collision_pair[1])

                collision_pair[0].move()
                collision_pair[1].move()
                continue

            # check_boundary_collision(ball)
            ball.move()

        for ball in balls:
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(6000)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
