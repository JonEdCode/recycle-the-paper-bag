import pgzrun
import random
WIDTH = 1000
HEIGHT = 600
TITLE = "recycle_paper_bag " 
gameover = False
actors = []
trash = ["bottle","battery","chips","bag"]
level = 1
total_lv = 5
animations = []
def draw():
    global actors 
    screen.blit("eco friendly bg",(0,0))
    if gameover == True:
        screen.draw.text("game over",(400,300),fontsize = 100)
    for actor in actors:
        actor.draw()
    
def game_over():
    global gameover 
    gameover = True
def actors_but_better():
    global actors , animations
      
    actors = []
    animations = []
    images = ["paper_bag"]
    for i in range(level):
        item = random.choice(trash)
        images.append(item)
    print(images)
    for i in range(level + 1):
        item = Actor(images[i])
        actors.append(item)
    gaps = level +2
    gap_size = 1000 // gaps
    random.shuffle(actors)
    for i in range(level +1):
        actors[i].pos = (i +1) *gap_size,100
    for actor in actors:
        animation = animate(actor,y = 600,duration = 5,on_finished = game_over)
        animations.append(animation)

def on_mouse_down(pos):
   global level 
   for actor in actors:
    if actor.collidepoint(pos):
        if actor.image == "paper_bag":
            level = level +1
            stop()
            actors_but_better()
        else:
            game_over()
def stop():
    global animations
    for animation in animations:
        if animation.running:
            animation.stop()

def update():
    pass
actors_but_better()









pgzrun.go()
