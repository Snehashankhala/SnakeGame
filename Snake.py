import pygame
import random


pygame.init()

colour_1 = (255, 255, 255)   
colour_2 = (255, 255, 102)   
colour_3 = (0, 0, 0)         
colour_4 = (213, 200, 80)    
colour_5 = (0, 255, 0)       
colour_6 = (255, 0, 0)      


box_len = 900
box_height = 600
screen = pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption("SNAKE GAME")


clock = pygame.time.Clock()
snake_block = 20             
snake_speed = 14


font = pygame.font.SysFont("arial", 30, True)
score_font = pygame.font.SysFont("arial", 45, True)


def final_score(score):
    value = score_font.render("Score: " + str(score), True, colour_2)
    screen.blit(value, [10, 10])


def make_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, colour_3, [x[0], x[1], block_size, block_size])


def display_msg(msg, color):
    mssg = font.render(msg, True, color)
    screen.blit(mssg, [box_len / 6, box_height / 3])


def game_start():
    game_over = False
    game_close = False

    x1 = box_len // 2
    y1 = box_height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

   
    foodx = random.randrange(0, box_len - snake_block, snake_block)
    foody = random.randrange(0, box_height - snake_block, snake_block)

    while not game_over:

        while game_close:
            screen.fill(colour_6)
            display_msg("You Lost! Press Y to Play Again or N to Quit", colour_4)
            final_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_y:
                        game_start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

      
        if x1 >= box_len or x1 < 0 or y1 >= box_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(colour_6)

       
        pygame.draw.rect(screen, colour_5, [foodx, foody, snake_block, snake_block])

       
        snake_head = [int(x1), int(y1)]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

       
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        make_snake(snake_block, snake_list)
        final_score(snake_length - 1)
        pygame.display.update()

      
        if abs(x1 - foodx) < snake_block and abs(y1 - foody) < snake_block:
            foodx = random.randrange(0, box_len - snake_block, snake_block)
            foody = random.randrange(0, box_height - snake_block, snake_block)
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_start()
