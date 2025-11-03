from pico2d import *

from bird import Bird
import game_world

import game_framework

bird = None

def handle_events():

def init():

def update():


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass