import pygame
import animals

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
total_time = 0

simba = animals.Simba()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    simba.rect.x = min(100 * (total_time + 1), 800)
    screen.blit(simba.image, simba.rect)

    pygame.display.update()

    total_time += clock.tick(60) / 1000

pygame.quit()
