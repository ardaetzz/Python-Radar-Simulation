import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 1080, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RADAR")

BLACK = (0,0,0)
GREEN = (0,255,0)
DARK_GREEN = (0,100,0)
RED = (255,0,0)

center = (WIDTH // 2, HEIGHT // 2)
radius = 250

clock = pygame.time.Clock()
angle = 0

line_length = radius

fade_amount = 10

def draw_radar(enemy_detected):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.set_alpha(fade_amount)
    fade_surface.fill(BLACK)
    screen.blit(fade_surface, (0,0))

    for i in range(1,6):
        pygame.draw.circle(screen, DARK_GREEN, center, i * radius // 5, 1)
    
    for i in range(0,360,45):
        x = center[0] + radius * math.cos(math.radians(i))
        y = center[1] + radius * math.sin(math.radians(i))
        pygame.draw.line(screen, DARK_GREEN, center, (x,y), 1)
    
    end_x = center[0] + line_length * math.cos(math.radians(angle))
    end_y = center[1] + line_length * math.sin(math.radians(angle))
    line_color = RED if enemy_detected else GREEN
    pygame.draw.line(screen, line_color, center, (end_x, end_y), 2)

    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    angle += 1
    if angle >= 360:
        angle = 0
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    end_x = center[0] + line_length * math.cos(math.radians(angle))
    end_y = center[1] + line_length * math.sin(math.radians(angle))
    distance_to_line = abs((end_y - center[1]) * mouse_x - (end_x - center[0]) * mouse_y + end_x * center[1] - end_y * center[0]) / math.sqrt((end_y - center[1]) ** 2 + (end_x - center[0]) ** 2)
    enemy_detected = distance_to_line < 5 and math.dist(center, (mouse_x, mouse_y)) <= radius
    

    draw_radar(enemy_detected)

    clock.tick(60)