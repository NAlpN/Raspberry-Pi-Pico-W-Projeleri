from machine import Pin, time_pulse_us
import utime
import math
import pygame

TRIGGER_PIN = 15
ECHO_PIN = 14

# Pygame ayarları
pygame.init()
WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
CENTER = (WIDTH // 2, HEIGHT)
RADIUS = 250
angle = 0
distance = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar Ekranı")
clock = pygame.time.Clock()

trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def measure_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    
    duration = time_pulse_us(echo, 1, 30000)
    distance = (duration / 2) * 0.0343
    return distance

running = True
while running:
    screen.fill(BLACK)

    distance = measure_distance()
    
    pygame.draw.arc(screen, GREEN, (CENTER[0] - RADIUS, CENTER[1] - RADIUS, RADIUS * 2, RADIUS * 2), math.radians(0), math.radians(180), 2)
    
    pygame.draw.arc(screen, GREEN, (CENTER[0] - RADIUS // 2, CENTER[1] - RADIUS // 2, RADIUS, RADIUS), math.radians(0), math.radians(180), 1)
    pygame.draw.arc(screen, GREEN, (CENTER[0] - RADIUS // 4, CENTER[1] - RADIUS // 4, RADIUS // 2, RADIUS // 2), math.radians(0), math.radians(180), 1)
    
    pygame.draw.line(screen, GREEN, (CENTER[0] - RADIUS, CENTER[1]), (CENTER[0] + RADIUS, CENTER[1]), 1)
    pygame.draw.line(screen, GREEN, CENTER, (CENTER[0], CENTER[1] - RADIUS), 1)

    if distance < 200:
        intensity = max(50, min(255, int(255 - (distance * 1.5))))
        radar_angle = angle % 180
        obj_x = CENTER[0] + distance * math.cos(math.radians(radar_angle))
        obj_y = CENTER[1] - distance * math.sin(math.radians(radar_angle))
        pygame.draw.circle(screen, (intensity, intensity, 0), (int(obj_x), int(obj_y)), 5)
    
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

    clock.tick(30)

pygame.quit()
