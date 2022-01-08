import os
import pygame
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load Images
ROCK_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "Rock.png")), (270, 270))
PAPER_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "Paper.png")), (270, 270))
SCISSORS_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "Scissors.png")), (270, 270))


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 900
        self.HEIGHT = 500
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rock-Paper-Scissors!")

        self.comp_turns = [ROCK_IMG, PAPER_IMG, SCISSORS_IMG]
        self.comp_turn = random.choice(self.comp_turns)

        self.player_turns = ["ROCK", "PAPER", "SCISSORS"]
        self.player_turn = ""

        # Winner Text Initializing
        self.WINNER_TEXT = pygame.font.SysFont("cambria", 60)

    def text(self):
        # Text Initializing
        TITLE_FONT = pygame.font.SysFont("cambria", 60)
        IMG_FONT = pygame.font.SysFont("cambria", 45)

        # Text Rendering
        title_text = TITLE_FONT.render("CHOOSE YOUR MOVE!", 1, BLACK)
        rock_text = IMG_FONT.render("ROCK", 1, BLACK)
        paper_text = IMG_FONT.render("PAPER", 1, BLACK)
        scissors_text = IMG_FONT.render("SCISSORS", 1, BLACK)

        # Text Blitting
        self.WIN.blit(title_text, (148, 13.5))
        self.WIN.blit(rock_text, (96, 430))
        self.WIN.blit(paper_text, (385, 430))
        self.WIN.blit(scissors_text, (656, 430))

    def result_screen(self):
        self.WIN.fill(WHITE)

        # Borders
        pygame.draw.line(self.WIN, BLACK, (0, 100), (self.WIDTH, 100), 5)
        pygame.draw.line(self.WIN, BLACK, (self.WIDTH / 2, 100),
                         (self.WIDTH / 2, self.HEIGHT), 5)
        pygame.draw.line(self.WIN, BLACK, (0, 415), (self.WIDTH, 415), 5)

        pygame.draw.line(self.WIN, BLACK, (0, 0), (self.WIDTH, 0), 7)
        pygame.draw.line(self.WIN, BLACK, (0, 0), (0, self.HEIGHT), 7)
        pygame.draw.line(self.WIN, BLACK, (self.WIDTH, 0),
                         (self.WIDTH, self.HEIGHT), 7)
        pygame.draw.line(self.WIN, BLACK, (0, self.HEIGHT),
                         (self.WIDTH, self.HEIGHT), 7)
        self.result_screen_text()
        pygame.display.update()

    def result_screen_text(self):
        # Text Initializing
        PLAYER_TEXT = pygame.font.SysFont("cambria", 45)
        COMP_TEXT = pygame.font.SysFont("cambria", 45)

        # Text Rendering
        player_text = PLAYER_TEXT.render("PLAYER", 1, BLACK)
        comp_text = COMP_TEXT.render("COMPUTER", 1, BLACK)

        # Text Blitting
        self.WIN.blit(comp_text, (107, 427))
        self.WIN.blit(player_text, (597, 427))

    def check_winner(self):
        if self.comp_turn == ROCK_IMG and self.player_turn == "ROCK":
            self.WIN.blit(ROCK_IMG, (90, 122))
            self.WIN.blit(ROCK_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("DRAW!", 1, BLACK)
            self.WIN.blit(self.winner_text, (360, 13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

        elif self.comp_turn == ROCK_IMG and self.player_turn == "PAPER":
            self.WIN.blit(ROCK_IMG, (90, 122))
            self.WIN.blit(PAPER_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("PLAYER WON!", 1, BLACK)
            self.WIN.blit(self.winner_text, (263,13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

        elif self.comp_turn == ROCK_IMG and self.player_turn == "SCISSORS":
            self.WIN.blit(ROCK_IMG, (90, 122))
            self.WIN.blit(SCISSORS_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("COMPUTER WON!", 1, BLACK)
            self.WIN.blit(self.winner_text, (212, 13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

        elif self.comp_turn == PAPER_IMG and self.player_turn == "ROCK":
            self.WIN.blit(PAPER_IMG, (90, 122))
            self.WIN.blit(ROCK_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("COMPUTER WON!", 1, BLACK)
            self.WIN.blit(self.winner_text, (212, 13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

        elif self.comp_turn == PAPER_IMG and self.player_turn == "PAPER":
            self.WIN.blit(PAPER_IMG, (90, 122))
            self.WIN.blit(PAPER_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("DRAW!", 1, BLACK)
            self.WIN.blit(self.winner_text, (360, 13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

        elif self.comp_turn == PAPER_IMG and self.player_turn == "SCISSORS":
            self.WIN.blit(PAPER_IMG, (90, 122))
            self.WIN.blit(SCISSORS_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("PLAYER WON!", 1, BLACK)
            self.WIN.blit(self.winner_text, (263, 13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

        elif self.comp_turn == SCISSORS_IMG and self.player_turn == "ROCK":
            self.WIN.blit(SCISSORS_IMG, (90, 122))
            self.WIN.blit(ROCK_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("PLAYER WON!", 1, BLACK)
            self.WIN.blit(self.winner_text, (263, 13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

        elif self.comp_turn == SCISSORS_IMG and self.player_turn == "PAPER":
            self.WIN.blit(SCISSORS_IMG, (90, 122))
            self.WIN.blit(PAPER_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("COMPUTER WON!", 1, BLACK)
            self.WIN.blit(self.winner_text, (212, 13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

        elif self.comp_turn == SCISSORS_IMG and self.player_turn == "SCISSORS":
            self.WIN.blit(SCISSORS_IMG, (90, 122))
            self.WIN.blit(SCISSORS_IMG, (540, 122))
            self.winner_text = self.WINNER_TEXT.render("DRAW!", 1, BLACK)
            self.WIN.blit(self.winner_text, (360, 13.5))
            pygame.display.update()
            pygame.time.delay(2200)
            self.main()

    def click_event(self):
        x, y = pygame.mouse.get_pos()

        for self.player_turn in self.player_turns:
            if ((x > 15 and x < 280) and (y > 120 and y < 390)):
                self.player_turn = "ROCK"
                print("ROCK")
                self.result_screen()
                self.check_winner()
                break

            elif ((x > 315 and x < 580) and (y > 120 and y < 390)):
                self.player_turn = "PAPER"
                print("PAPER")
                self.result_screen()
                self.check_winner()
                break

            elif ((x > 615 and x < 880) and (y > 120 and y < 390)):
                self.player_turn = "SCISSORS"
                print("SCISSORS")
                self.result_screen()
                self.check_winner()
                break

    def draw_window(self):
        self.WIN.fill(WHITE)
        self.WIN.blit(ROCK_IMG, (15, 120))
        self.WIN.blit(PAPER_IMG, (316, 120))
        self.WIN.blit(SCISSORS_IMG, (615, 120))

        # Borders
        pygame.draw.line(self.WIN, BLACK, (0, 100), (self.WIDTH, 100), 5)
        pygame.draw.line(self.WIN, BLACK, (300, 100), (300, self.HEIGHT), 5)
        pygame.draw.line(self.WIN, BLACK, (600, 100), (600, self.HEIGHT), 5)
        pygame.draw.line(self.WIN, BLACK, (0, 415), (self.WIDTH, 415), 5)

        pygame.draw.line(self.WIN, BLACK, (0, 0), (self.WIDTH, 0), 7)
        pygame.draw.line(self.WIN, BLACK, (0, 0), (0, self.HEIGHT), 7)
        pygame.draw.line(self.WIN, BLACK, (self.WIDTH, 0),
                         (self.WIDTH, self.HEIGHT), 7)
        pygame.draw.line(self.WIN, BLACK, (0, self.HEIGHT),
                         (self.WIDTH, self.HEIGHT), 7)

        self.text()

        pygame.display.update()

    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            self.comp_turn = random.choice(self.comp_turns)
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_event()
            self.draw_window()
        pygame.quit()


if __name__ == "__main__":
    Game().main()
