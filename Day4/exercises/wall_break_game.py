import pygame
import sys
import random

# Pygame 초기화 (Initialize pygame)
pygame.init()

# 화면 설정 (View setting)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker Game")

# 색상 정의 (Color setting)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들 변수 (Paddle variables)
paddle_width = 100
paddle_height = 10
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = SCREEN_HEIGHT - 30
paddle_speed = 7

# 공 변수 (Ball variables)
ball_radius = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = random.choice([-4, 4])
ball_speed_y = -4

# 벽돌 변수 (Brick variables)
brick_rows = 5
brick_cols = 8
brick_width = SCREEN_WIDTH // brick_cols
brick_height = 30
bricks = []


# TODO: make blocks using bricks.append function and pygame.Rect function
for row in range(brick_rows):
    for col in range(brick_cols):  
        pass # bricks.append(pygame.Rect(col * brick_width, row * brick_height, brick_width - 5, brick_height - 5))


# 점수 변수 (Score variables)
score = 0
font = pygame.font.Font(None, 36)

# 게임 루프 (Game FPS setting)
clock = pygame.time.Clock() 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력 처리 (Key strock)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - paddle_width:
        paddle_x += paddle_speed

    # 공 이동 (Ball movement)
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공 화면 경계 충돌 처리 (Ball Collision with border)
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# TODO: Paddle Ball colliding effect; when ball collide with paddle, ball's y direction speed changes. 
    if paddle.colliderect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2):
        pass #ball_speed_y = -ball_speed_y

# TODO: Brick Ball colliding effect; 
    # Task1: remove collided brick
    # Task2: change ball's y-axis speed direction
    # Task3: increase score by 10
    for brick in bricks[:]:
        if brick.colliderect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2):
            # bricks.remove(brick)
            # ball_speed_y = -ball_speed_y
            # score += 10
            break

    # 공 바닥에 닿았을 때 게임 오버
    if ball_y > SCREEN_HEIGHT:
        print("Game Over! Your score:", score)
        pygame.quit()
        sys.exit()

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, BLUE, paddle)

    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
