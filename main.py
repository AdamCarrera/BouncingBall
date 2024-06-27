"""
Main file for bouncing ball simulator
"""
import sys
import pygame
from settings import WIDTH, HEIGHT, BACKGROUND_COLOR, BALL_CONFIG, Boundary
from ball import Ball


def main():
    """
    Set up and run simulation
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball Simulation")
    clock = pygame.time.Clock()

    ball = Ball(BALL_CONFIG)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for line in Boundary:
            pygame.draw.line(screen, (255, 255, 0), *line.value, 5)

        ball.color = (255, 0, 0) if any(ball.collider.clipline(*line.value)
                                        for line in Boundary) else (0, 255, 0)

        # for line in Boundary:
        #     clipline = ball.collider.clipline(*line.value)
        #     print(f"collider center: {ball.collider.center}")
        #     if clipline:
        #         print(f"clipline: {clipline}")

        ball.move()
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
