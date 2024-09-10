import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
SKYBLUE = (135, 206, 235)

#Background
display_surface.fill(SKYBLUE)

#Sun
TOP_LEFT = (60, 50)
RADIUS = 100
pygame.draw.circle(display_surface, YELLOW, TOP_LEFT, RADIUS)

#Cloud
PLACE = (400, 50)
RADIUS = 40
pygame.draw.circle(display_surface, WHITE, PLACE, RADIUS)
#Cloud
PLACE = (370, 40)
RADIUS = 40
pygame.draw.circle(display_surface, WHITE, PLACE, RADIUS)
#Cloud
PLACE = (406, 20)
RADIUS = 40
pygame.draw.circle(display_surface, WHITE, PLACE, RADIUS)
#Cloud
PLACE = (388, 1)
RADIUS = 40
pygame.draw.circle(display_surface, WHITE, PLACE, RADIUS)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()