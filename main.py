# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import Box2D
from Box2D.b2 import (world, polygonShape, staticBody, dynamicBody)

SCREEN_WIDTH=1450
SCREEN_HEIGHT=720

PPM = 10.0

TARGET_FPS = 60

TIME_STEP = 1/TARGET_FPS

sub_step_count = 4

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

world = world(gravity=(0, -10), doSleep=True)

ground_body = world.CreateStaticBody(
    position=(100, 2),
    shapes=polygonShape(box=(100, 2))
)

circle_body = world.CreateDynamicBody(position=(10, 200))
circle_fixture = circle_body.CreateCircleFixture(radius=1, density=5, friction=0.3, restitution=0.2)

box_body = world.CreateDynamicBody(position=(11, 4))
box_fixture = box_body.CreatePolygonFixture(box=(1, 1), density=1, friction=0.3, restitution=0.5)

box_body_2 = world.CreateDynamicBody(position=(9, 4))
box_fixture_2 = box_body_2.CreatePolygonFixture(box=(1, 1), density=1, friction=0.3, restitution=0.5)

box_body_3 = world.CreateDynamicBody(position=(10, 6))
box_fixture_3 = box_body_3.CreatePolygonFixture(box=(1, 1), density=1, friction=0.3, restitution=0.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill((0,0,0))

    world.Step(TIME_STEP, sub_step_count, 10)

    for fixture in ground_body.fixtures:
        shape = fixture.shape
        vertices = [(ground_body.transform * v)*PPM for v in shape.vertices]
        vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
        pygame.draw.polygon(screen, (255, 0, 0), vertices)

    for fixture in box_body_2.fixtures:
        shape = fixture.shape
        vertices = [(box_body_2.transform * v)*PPM for v in shape.vertices]
        vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
        pygame.draw.polygon(screen, (0, 255, 0), vertices)

    for fixture in box_body_3.fixtures:
        shape = fixture.shape
        vertices = [(box_body_3.transform * v)*PPM for v in shape.vertices]
        vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
        pygame.draw.polygon(screen, (0, 255, 0), vertices)

    for fixture in circle_body.fixtures:
        shape = fixture.shape
        position = circle_body.transform * shape.pos * PPM
        position = (position[0], SCREEN_HEIGHT - position[1])
        pygame.draw.circle(screen, (0, 0, 255), [int(x) for x in position], int(shape.radius*PPM))

    for fixture in box_body.fixtures:
        shape = fixture.shape
        vertices = [(box_body.transform * v)*PPM for v in shape.vertices]
        vertices = [(v[0], SCREEN_HEIGHT-v[1]) for v in vertices]
        pygame.draw.polygon(screen, (0, 255, 0), vertices)

    clock.tick(TARGET_FPS)

    pygame.display.update()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
