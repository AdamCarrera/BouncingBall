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

    for ball in balls:
        ball.velocity = Velocity.random()
        print(ball.velocity)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for line in Boundary:
            pygame.draw.line(screen, (255, 255, 0), *line.value, 5)

        # ball.color = RGBColor(255, 0, 0) \
        #     if any(
        # ball.collider.clipline(*line.value) for line in Boundary) \
        #     else RGBColor(0, 255, 0)

        # for line in Boundary:
        #     clipline = ball.collider.clipline(*line.value)
        #     print(f"collider center: {ball.collider.center}")
        #     if clipline:
        #         print(f"clipline: {clipline}")

        for ball in balls:
            ball.move()
            ball.draw(screen)

            collision_pair = check_collision(balls)
            if collision_pair:
                calculate_collision(collision_pair[0], collision_pair[1])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
