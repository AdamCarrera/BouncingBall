"""
Main file for bouncing ball simulator
"""
import sys
import pygame
from settings import (
    Boundary,
    Velocity,
    create_config,
    WIDTH,
    HEIGHT,
    BACKGROUND_COLOR,
    N_BALLS
)
from ball import Ball, check_collision, calculate_collision


def main():
    """
    Set up and run simulation
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball Simulation")
    clock = pygame.time.Clock()

    balls = [Ball(create_config()) for _ in range(N_BALLS)]
    has_collided = False

    for ball in balls:
        ball.velocity = Velocity.random()
        print(ball.velocity)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # print(balls[0].velocity)

        for line in Boundary:
            pygame.draw.line(screen, (255, 255, 0), *line.value, 5)

        # go through each ball and check if there's a collision
        # if there is, update speed then move
        # if there isnt, move
        for ball in balls:
            collision_pair = check_collision(balls)

            # we only want to update the speed
            # if we haven't collided recently
            if collision_pair and not has_collided:
                calculate_collision(collision_pair[0], collision_pair[1])
                has_collided = True

            # has_collided stays true until collision_pair evaluates to false
            if collision_pair and has_collided:
                has_collided = True

            if not collision_pair:
                has_collided = False

            ball.move()
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
