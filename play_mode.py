from pico2d import *

from bird import Bird
import game_world

import game_framework

bird = None

def handle_events():

def init():
    global bird

    running = True
    bird = Bird()
    game_world.add_object(bird, 1)

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass