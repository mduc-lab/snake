import pygame
import random
import sys

# Initialize the game
pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# khai bao ham
# ham kiem tra va cham
def check_collision(snake_body):
    if snake_x < 0 or snake_x >= 400 or snake_y < 0 or snake_y >= 400:
        return False
    if (snake_x, snake_y) in snake_body[:-1]:
        return False
    #print(snake_x, snake_y)
    #print(snake_body[:-1])
    return True

def score_display(score):
    score_suface = game_font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_suface, (10, 10))

# khai bao bien

game_font = pygame.font.Font('flappy/04B_19.TTF',20)
score = 0
# thong so ran
snake_part = 20
snake_x = snake_y = 200
x_change = y_change = 0
snake_speed = 2
snake_length = 1
snake_body = []

# thong so thuc an
food_x = random.randint(0, 19) * snake_part
food_y = random.randint(0, 19) * snake_part


# Game loop
game_active = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -1
                x_change = 0
            if event.key == pygame.K_DOWN:
                y_change = 1
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 1
                y_change = 0
            if event.key == pygame.K_SPACE:
                if game_active == False:
                    game_active = True
                    snake_x = snake_y = 200
                    x_change = y_change = 0
                    snake_length = 1
                    snake_body = []
                    score = 0
    # clear screen
    screen.fill((0, 0, 0))

    if game_active:
        # di chuyen ran
        snake_x += x_change * snake_part
        snake_y += y_change * snake_part

        # them than ran
        snake_body.append((snake_x, snake_y))
        if len(snake_body) > snake_length:
            del snake_body[0]
        if snake_x == food_x and snake_y == food_y:
            snake_length += 1
            score+=1
            food_x = random.randint(0, 19) * snake_part
            food_y = random.randint(0, 19) * snake_part
        # ve ran
        for x, y in snake_body:
            pygame.draw.rect(screen, (255, 255, 255), (x, y, snake_part, snake_part))

        # ve thuc an
        for x, y in [(food_x, food_y)]:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, snake_part, snake_part))

        
        score_display(score)
        game_active = check_collision(snake_body)
    else:
        game_over_surface = game_font.render('GAME OVER', True, (255, 255, 255))
        screen.blit(game_over_surface, (100, 200))

    # update screen
    pygame.display.update()
    clock.tick(snake_speed)
