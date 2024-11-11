import pgzrun
import random
WIDTH = 1000
HEIGHT = 600
TITLE = "recycle_paper_bag " 
actors = []
trash = ["bottle","battery","chips","bag"]
level = 1
total_lv = 5
def draw():
    global actors 
    screen.blit("eco friendly bg",(0,0))
    for actor in actors:
        actor.draw()
def actors_but_better():
    global actors
    images = ["paper_bag"]
    for i in range(level):
        item = random.choice(trash)
        images.append(item)
    print(images)
    for i in range(level + 1):
        item = Actor(images[i])
        actors.append(item)
def update():
    pass
actors_but_better()








pgzrun.go()
