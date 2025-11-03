from pico2d import *

from bird import Bird
import game_world

import game_framework

bird = None

def handle_events():
    global runnung

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            bird.handle_event(event)

def init():
    global bird

    running = True
    bird = Bird()
    game_world.add_object(bird, 1)

def update():
    game_world.update()
    delay(0.1)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass