import pgzrun
import random

WIDTH = 600
HEIGHT = 500

score = 0
bee_dead = False

bee = Actor("flower")
bee.pos = 100, 100

flower = Actor("bee")
flower.pos = 200, 200

def draw():
    screen.blit("sky", (0, 0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+ str(score), center = (300, 50), fontsize = 31)
    if bee_dead==True:
        screen.fill("SteelBlue3")
        screen.draw.text(("Bee died! Your final score: ")+str(score), center = (330, 50), fontsize = 32)



def spawn_flower():
    flower.x = random.randint(70, (WIDTH-70))
    flower.y = random.randint(70, (HEIGHT-70))

def update():
    global score
    if keyboard.w:
        bee.y = bee.y + 1
    if keyboard.s:
        bee.y = bee.y - 1
    if keyboard.a:
        bee.x = bee.x + 1
    if keyboard.d:
        bee.x = bee.x - 1
    if flower.colliderect(bee):
        spawn_flower()
        score = score+1

def time_up():
    global bee_dead
    bee_dead = True

clock.schedule(time_up, 20.1)





pgzrun.go()