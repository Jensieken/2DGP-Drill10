from pico2d import load_image, get_time, load_font
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

import game_world
import game_framework
from state_machine import StateMachine

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

time_out = lambda e: e[0] == 'TIMEOUT'

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


class Idle:
    def __init__(self, bird):
        self.bird = bird

    def enter(self, e):
        self.bird.wait_time = get_time()
        self.bird.dir = 0

    def exit(self, e):
        pass

    def do(self):
        self.bird.frame = (self.bird.frame + 1) % 8
        if get_time() - self.bird.wait_time > 3:
            self.bird.state_machine.handle_state_event(('TIMEOUT', None))

    def draw(self):
        if self.bird.face_dir == 1: # right
            self.bird.image.clip_draw(self.bird.frame * 100, 300, 100, 100, self.bird.x, self.bird.y)
        else: # face_dir == -1: # left
            self.bird.image.clip_draw(self.bird.frame * 100, 200, 100, 100, self.bird.x, self.bird.y)

class Run:
    def __init__(self, bird):
        self.bird = bird

    def enter(self, e):
        if right_down(e):
            self.bird.dir += 1
        elif left_down(e):
            self.bird.dir -= 1
        elif right_up(e):
            self.bird.dir -= 1
        elif left_up(e):
            self.bird.dir += 1

    def exit(self, e):
        pass

    def do(self):
        pass

    def draw(self):


class Bird:

