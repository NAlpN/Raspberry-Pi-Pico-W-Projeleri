import pygame
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar Ekranı")

CENTER = (300, 600)
RADIUS = 300

angle = 0

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    pygame.draw.arc(screen, GREEN, (CENTER[0] - RADIUS, CENTER[1] - RADIUS, RADIUS * 2, RADIUS * 2), math.radians(0), math.radians(180), 2)

    pygame.draw.arc(screen, DARK_GREEN, (CENTER[0] - RADIUS // 2, CENTER[1] - RADIUS // 2, RADIUS, RADIUS), math.radians(0), math.radians(180), 1)
    pygame.draw.arc(screen, DARK_GREEN, (CENTER[0] - RADIUS // 4, CENTER[1] - RADIUS // 4, RADIUS // 2, RADIUS // 2), math.radians(0), math.radians(180), 1)

    pygame.draw.line(screen, DARK_GREEN, (CENTER[0] - RADIUS, CENTER[1]), (CENTER[0] + RADIUS, CENTER[1]), 1)
    pygame.draw.line(screen, DARK_GREEN, CENTER, (CENTER[0], CENTER[1] - RADIUS), 1)

    end_x = CENTER[0] + RADIUS * math.cos(math.radians(angle))
    end_y = CENTER[1] - RADIUS * math.sin(math.radians(angle))
    
    pygame.draw.line(screen, GREEN, CENTER, (end_x, end_y), 2)
    
    angle += 1
    if angle > 180:
        angle = 0

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()