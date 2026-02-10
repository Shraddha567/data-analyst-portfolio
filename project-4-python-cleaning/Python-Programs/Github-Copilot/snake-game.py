import pygame

import random
from enum import Enum
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20

# Colors
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
GREEN = (34, 177, 76)
DARK_GREEN = (22, 115, 50)
GRAY = (50, 50, 50)
YELLOW = (255, 215, 0)

# Direction enum
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)
        self.body.insert(0, new_head)

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return True
        if head in self.body[1:]:
            return True
        return False

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

    def respawn(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

# Main game function
def draw_score(screen, font, score, high_score):
    """Draw score on the screen"""
    score_text = font.render(f"Score: {score}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, YELLOW)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 40))

def draw_start_screen(screen, font, big_font):
    """Draw the start screen"""
    screen.fill(BLACK)
    
    title = big_font.render("SNAKE GAME", True, GREEN)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(title, title_rect)
    
    instructions = [
        "Use ARROW KEYS to control the snake",
        "Eat RED food to grow and score points",
        "Don't hit the walls or yourself!",
        "",
        "Press SPACE to START",
        "Press Q to QUIT"
    ]
    
    instruction_font = pygame.font.Font(None, 24)
    y_offset = SCREEN_HEIGHT // 2 - 60
    
    for instruction in instructions:
        text = instruction_font.render(instruction, True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
        screen.blit(text, text_rect)
        y_offset += 40
    
    pygame.display.flip()

def draw_game_over_screen(screen, font, big_font, score, high_score):
    """Draw the game over screen"""
    screen.fill(BLACK)
    
    game_over = big_font.render("GAME OVER", True, RED)
    game_over_rect = game_over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(game_over, game_over_rect)
    
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    screen.blit(score_text, score_rect)
    
    high_score_text = font.render(f"High Score: {high_score}", True, YELLOW)
    high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(high_score_text, high_score_rect)
    
    restart_text = pygame.font.Font(None, 24).render("Press SPACE to play again or Q to quit", True, WHITE)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    screen.blit(restart_text, restart_rect)
    
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game - Professional Edition")
    clock = pygame.time.Clock()
    
    font = pygame.font.Font(None, 32)
    big_font = pygame.font.Font(None, 72)
    
    high_score = 0
    game_state = "start"  # start, playing, game_over
    
    while True:
        if game_state == "start":
            draw_start_screen(screen, font, big_font)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = "playing"
                        snake = Snake()
                        food = Food()
                        score = 0
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        
        elif game_state == "playing":
            clock.tick(10)  # 10 FPS
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and snake.direction != Direction.DOWN:
                        snake.next_direction = Direction.UP
                    elif event.key == pygame.K_DOWN and snake.direction != Direction.UP:
                        snake.next_direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT and snake.direction != Direction.RIGHT:
                        snake.next_direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT and snake.direction != Direction.LEFT:
                        snake.next_direction = Direction.RIGHT
            
            snake.direction = snake.next_direction
            snake.move()
            
            if snake.body[0] == food.position:
                snake.grow()
                food.respawn()
                score += 1
            
            if snake.check_collision():
                if score > high_score:
                    high_score = score
                game_state = "game_over"
            
            # Draw everything
            screen.fill(BLACK)
            
            # Draw border
            pygame.draw.rect(screen, GRAY, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 3)
            
            # Draw snake
            for i, segment in enumerate(snake.body):
                if i == 0:  # Head
                    pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(screen, DARK_GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE), 2)
                else:  # Body
                    pygame.draw.rect(screen, DARK_GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE), 1)
            
            # Draw food
            pygame.draw.rect(screen, RED, (food.position[0], food.position[1], GRID_SIZE, GRID_SIZE))
            pygame.draw.circle(screen, YELLOW, 
                             (food.position[0] + GRID_SIZE // 2, food.position[1] + GRID_SIZE // 2), 3)
            
            draw_score(screen, font, score, high_score)
            
            pygame.display.flip()
        
        elif game_state == "game_over":
            draw_game_over_screen(screen, font, big_font, score, high_score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = "start"
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    main()
