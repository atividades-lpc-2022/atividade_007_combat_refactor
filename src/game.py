import pygame
from modules.Brick import Brick
from modules.Coordinate import Coordinate
from modules.Dimension import Dimension
from modules.HUD import HUD
from modules.Score import Score
from modules.Tank import Tank
from modules.Screen import Screen
from modules.Boundary import Boundary
from modules.Ball import Ball
from config import Config


class Game:
    def __init__(self, config: Config):
        self.is_running = True
        self.player_1_score = Score()
        self.player_2_score = Score()
        self.config = config
        self.balls: list[Ball] = []
        self.bricks: list[Brick] = []

        # Create screen
        self.screen = Screen(
            Dimension(self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT),
            self.config.COLORS["GREEN"],
        )

        # Players
        self.tank_1 = Tank(
            Coordinate(self.config.SCREEN_WIDTH * 0.1, 320),
            self.config.SPRITES_PATH["PLAYER_1"],
            1,
            self.screen.dimension.width,
            self.screen.dimension.height,
        )
        self.tank_2 = Tank(
            Coordinate(self.config.SCREEN_WIDTH * 0.9, 320),
            self.config.SPRITES_PATH["PLAYER_2"],
            2,
            self.screen.dimension.width,
            self.screen.dimension.height,
        )

        # HUD
        self.hud = HUD(self.config.FONT_PATH, self.config.FONT_SIZE)

        # Bricks
        for brick_x, brick_y, brick_w, brick_h in self.config.BRICKS_COORDINATES:
            self.bricks.append(
                Brick(
                    Coordinate(brick_x, brick_y),
                    Dimension(brick_w, brick_h),
                    self.config.COLORS["ORANGE"],
                )
            )

        # Boundaries
        self.boundary = Boundary(self.config.COLORS["ORANGE"])

    def stop(self):  # Stop game
        self.is_running = False

    def reset(self):  # Reset all status
        self.player_1_score.reset()
        self.player_2_score.reset()

    def use_global_events(self):  # Set global events (exit the game, ...)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def play(
        self,
    ):  # Implement game loop (draw all elements (Screen, HUD, Tanks, Bricks))

        # Initialize pygame inside game loop
        pygame.init()

        # Initialize mixer
        pygame.mixer.init()
        shot = pygame.mixer.Sound("src/sounds/shot.wav")

        pygame.display.set_caption("TANK PONG")
        clock = pygame.time.Clock()

        while self.is_running:
            self.use_global_events()

            self.screen.draw()
            self.tank_1.draw(self.screen)
            self.tank_2.draw(self.screen)

            self.hud.draw(
                self.screen,
                self.player_1_score,
                self.player_2_score,
                self.config.COLORS["RED"],
                self.config.COLORS["BLUE"],
            )

            for ball in self.balls:
                if ball.hits == self.config.MAX_BALL_HITS:
                    self.balls.remove(ball)

                if ball.is_colliding(self.tank_2.coordinate, self.tank_2.dimension):
                    if ball.player == 1:
                        self.player_1_score.increment()
                        self.balls.remove(ball)
                        self.tank_2.change_position()

                if ball.is_colliding(self.tank_1.coordinate, self.tank_1.dimension):
                    if ball.player == 2:
                        self.player_2_score.increment()
                        self.balls.remove(ball)
                        self.tank_1.change_position()

                for brick in self.bricks:
                    if ball.is_colliding(brick.coordinate, brick.dimension):
                        ball.y_velocity = -1
                        ball.x_velocity = -1

                ball.draw(self.screen)

            for brick in self.bricks:
                brick.draw(self.screen)

            self.boundary.draw(self.screen)

            # Tank 1's movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                has_collision = False
                for brick in self.bricks:
                    if self.tank_1.is_colliding(brick.coordinate, brick.dimension):
                        self.tank_1.coordinate.x -= 1
                        self.tank_1.coordinate.y -= 1
                        has_collision = True
                if not has_collision:
                    self.tank_1.move_up()

            if keys[pygame.K_a]:
                self.tank_1.rotate(45)
                pygame.time.delay(60)
            if keys[pygame.K_d]:
                self.tank_1.rotate(-45)
                pygame.time.delay(60)
            if keys[pygame.K_f]:
                has_ball = False
                for ball in self.balls:
                    if ball.player == 1:
                        has_ball = True
                if not has_ball:
                    new_ball = self.tank_1.fire(
                        self.config.COLORS["BLACK"], self.config.BALL_DRAW_VELOCITY
                    )
                    self.balls.append(new_ball)
                    shot.play()

            # Tank 2's movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                has_collision = False
                for brick in self.bricks:
                    if self.tank_2.is_colliding(brick.coordinate, brick.dimension):
                        self.tank_2.coordinate.x += 1.1
                        self.tank_2.coordinate.y -= 1.1
                        has_collision = True
                if not has_collision:
                    self.tank_2.move_up()

            if keys[pygame.K_LEFT]:
                self.tank_2.rotate(45)
                pygame.time.delay(60)
            if keys[pygame.K_RIGHT]:
                self.tank_2.rotate(-45)
                pygame.time.delay(60)
            if keys[pygame.K_SPACE]:
                has_ball = False
                for ball in self.balls:
                    if ball.player == 2:
                        has_ball = True
                if not has_ball:
                    new_ball = self.tank_2.fire(
                        self.config.COLORS["BLACK"], self.config.BALL_DRAW_VELOCITY
                    )
                    self.balls.append(new_ball)
                    shot.play()

            pygame.display.update()
            clock.tick(60)
