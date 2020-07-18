import pygame
import random

screen_size=[150,300]
screen=pygame.display.set_mode(screen_size)
pygame.font.init()

background=pygame.image.load("road.jpg")
user=pygame.image.load("user.png")
car=pygame.image.load("car.png")

score=0

def display_score(score):
    font = pygame.font.SysFont('Time New Romans', 20)
    score_text = 'Score: ' + str(score)
    text = font.render(score_text, True, (0,255,0))
    screen.blit(text, [20, 10])

def total_score():
    pygame.draw.rect(screen,(200,0,0), [30, 500, 500, 90])
    font = pygame.font.SysFont('Time New Romans', 20)
    score_text = 'Total Score: ' + str(score)
    text = font.render(score_text, True,(0,200,0))
    screen.blit(text, [30, 100])
    pygame.display.flip()
    pygame.time.delay(2500)

def crash(index):
    global alive
    total_score()
    alive=False

def random_num():
    return -1*random.randint(400,1000)

car_y=[random_num(),random_num(),random_num()]

user_x=55

def car_position(index):
    global score
    if car_y[index]>300:
        car_y[index]=random_num()
        score+=1
        print("Score:",score)
    else:
        car_y[index]+=3

alive=True
while alive:
    pygame.event.get()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x<105:
        user_x=user_x+2
    if keys[pygame.K_LEFT] and user_x>0:
        user_x=user_x-2

    car_position(0)
    car_position(1)
    car_position(2)

    clock=pygame.time.Clock()
    screen.blit(background,[0,0])
    screen.blit(user, [user_x, 240])
    screen.blit(car, [0, car_y[0]])
    screen.blit(car, [55, car_y[1]])
    screen.blit(car, [110, car_y[2]])

    if car_y[0]>200 and user_x<33:
        crash(0)
    if car_y[1] > 200 and user_x > 33 and user_x<80:
        crash(1)
    if car_y[2]>200 and user_x>80:
        crash(2)

    display_score(score)

    pygame.display.update()
    clock.tick(50)