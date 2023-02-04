import pygame
import random
import time


class Game:
    def __init__(self) -> None:
        # Load the assets
        self.balloon_img = pygame.image.load("./resources/balloon_purple.png")

        # Game Init
        pygame.font.init()

        # Game constants
        self.min_distance_between_balloon = 50
        self.spawn_interval = 1  # seconds

        # Game Variables
        self.popped_balloons = 0
        self.missed_balloons = 0
        self.last_spawn_time = time.time()
        self.balloon_width = self.balloon_img.get_width()
        self.distance_between_balloons = self.balloon_width + self.min_distance_between_balloon

        # Set up font
        self.score_font = pygame.font.Font(None, 30)

        # Set up the game window
        self.window_size = (1200, 1000)
        self.screen = pygame.display.set_mode(self.window_size)

        # Create the game objects
        self.balloons = []
        self.clock = pygame.time.Clock()

        pygame.init()
    

    def start_game(self):

        # Game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Spawn balloons
            if len(self.balloons) < 1 and time.time() - self.last_spawn_time >= self.spawn_interval:
                max_x = max(0, self.window_size[0] - 2 * self.distance_between_balloons)
                x = random.randint(0, max_x)
                y = self.window_size[1]
                self.balloons.extend([(x + i * self.distance_between_balloons, y) for i in range(1)])
                self.last_spawn_time = time.time()

            
            # Check if balloons are popped
            mouse_pos = pygame.mouse.get_pos()
            for i, b in enumerate(self.balloons):
                x, y = b
                if x < mouse_pos[0] < x + self.balloon_img.get_width() and y < mouse_pos[1] < y + self.balloon_img.get_height():
                    self.balloons.pop(i)
                    self.popped_balloons += 1
                    break
            
            # Update the game screen
            self.screen.fill((255, 255, 255))
            for i, (x, y) in enumerate(self.balloons):
                self.screen.blit(self.balloon_img, (x, y))
                y -= 3
                self.balloons[i] = (x, y)
            pygame.display.update()
            
            # Check if balloons have left the screen
            self.balloons = [b for b in self.balloons if b[1] > - self.balloon_img.get_height()]
            self.missed_balloons += 3 - len(self.balloons)
            
            # Show the score
            font = pygame.font.Font(None, 36)
            popped_text = font.render("Popped balloons: " + str(self.popped_balloons), True, (0, 0, 0))
            missed_text = font.render("Missed balloons: " + str(self.missed_balloons), True, (0, 0, 0))
            self.screen.blit(popped_text, (10, 10))
            self.screen.blit(missed_text, (self.window_size[0] - missed_text.get_width() - 10, 10))

            """ # Draw score
            score_font = pygame.font.Font(None, 30)
            popped_balloons_text = score_font.render("Popped Balloons: " + str(popped_balloons), True, (0, 0, 0))
            missed_balloons_text = score_font.render("Missed Balloons: " + str(missed_balloons), True, (0, 0, 0))

            screen.blit(popped_balloons_text, (10, 10))
            screen.blit(missed_balloons_text, (window_size[0] - 160, 10)) """
            
            pygame.display.update()
            
            # Control the game speed
            self.clock.tick(60)

        # Quit Pygame
        pygame.quit()


if __name__ =="__main__":
    balloonGame = Game()
    balloonGame. start_game()