import pygame
from random import randint, choice


# Define some colors
BACKGROUND_COLOR = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.randomize()

    def move(self):
        min_x, min_y = self.radius, self.radius
        max_x = SCREEN_WIDTH - self.radius
        max_y = SCREEN_HEIGHT - self.radius
        self.x = constrain(min_x, self.x + self.dx, max_x)
        self.y = constrain(min_y, self.y + self.dy, max_y)
        if self.x in (min_x, max_x):
            self.dx = -self.dx
        if self.y in (min_y, max_y):
            self.dy = -self.dy

    def randomize(self):
        self.dx, self.dy = 0, 0
        while self.dx == self.dy == 0:
            self.dx = randint(-3, +3)
            self.dy = randint(-3, +3)
        self.color = (randint(10, 255),
                      randint(10, 255),
                      randint(10, 255))


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.radius = 10
        self.color = (0, 0, 0)

    def move(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_DOWN]:
            dy += 1
        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1
        min_x, min_y = self.radius, self.radius
        max_x = SCREEN_WIDTH - self.radius
        max_y = SCREEN_HEIGHT - self.radius
        self.x = constrain(min_x, self.x + dx, max_x)
        self.y = constrain(min_y, self.y + dy, max_y)


def main():
    pygame.init()

    # Set the height and width of the screen
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Balls")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = []
    for i in range(1, 5):
        balls.append(Ball(100*i, 100*i,
                          randint(10, 70)))
    player = Player()

    # Loop until the user clicks the close button or ESC.
    done = False
    while not done:
        # Limit number of frames per second
        clock.tick(60)

        # Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_r:
                    choice(balls).randomize()
                elif event.key == pygame.K_a:
                    new = Ball(200, 200, randint(20, 50))
                    balls.append(new)

        # Move the objects
        for ball in balls:
            ball.move()

        player.move()

        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color,
                               (ball.x, ball.y), ball.radius)
        pygame.draw.circle(screen, player.color,
                           (player.x, player.y), player.radius)

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()


def constrain(small, value, big):
    """Return a new value which isn't smaller than small or larger than big"""
    return max(min(value, big), small)


if __name__ == "__main__":
    main()
