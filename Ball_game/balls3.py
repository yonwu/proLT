import pygame
import random

# Define some colors
BACKGROUND_COLOR = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def randomize(self):
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.dx = random.randint(-3, +3)
        self.dy = random.randint(-3, +3)

    def move(self):
        min_y = self.radius
        max_y = SCREEN_HEIGHT - self.radius
        self.y = constrain(min_y, self.y + self.dy, max_y)
        if self.y == max_y or self.y == min_y:
            self.dy = self.dy * (-1)

        min_x = self.radius
        max_x = SCREEN_WIDTH - self.radius
        self.x = constrain(min_x, self.x + self.dx, max_x)
        if self.x == max_x or self.x == min_x:
            self.dx = self.dx * (-1)


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.radius = 10
        self.color = (123, 123, 123)

    def move(self):
        move_x, move_y = 0, 0

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            move_y = 2
        if pygame.key.get_pressed()[pygame.K_UP]:
            move_y = -2
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            move_x = -2
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            move_x = 2

        min__player_y = self.radius
        max_palyer_y = SCREEN_HEIGHT - self.radius
        self.y = constrain(min__player_y, self.y + move_y, max_palyer_y)

        min__player_x = self.radius
        max_player_x = SCREEN_WIDTH - self.radius
        self.x = constrain(min__player_x, self.x + move_x, max_player_x)



def main():
    pygame.init()

    # Set the height and width of the screen
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Balls")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = []

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
                if event.key == pygame.K_z:
                    random_ball = random.choice(balls)
                    random_ball.randomize()
                elif event.key == pygame.K_a:
                    new_ball = Ball(50, 50, 25)
                    new_ball.randomize()
                    balls.append(new_ball)

        # Move a player
        player.move()

        # Move balls
        for ball in balls:
            ball.move()

        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color,
                               (ball.x, ball.y), ball.radius)

        pygame.draw.circle(screen, player.color, (player.x, player.y), player.radius)

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()


def constrain(small, value, big):
    """Return a new value which isn't smaller than small or larger than big"""
    value_list = [small, value, big]
    value_list.sort()

    return value_list[1]


if __name__ == "__main__":
    main()
