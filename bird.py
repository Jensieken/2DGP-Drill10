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

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 120.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Idle:
    def __init__(self, bird):
        self.bird = bird

    def enter(self, e):
        self.bird.wait_time = get_time()
        self.bird.dir = 0

    def exit(self, e):
        pass

    def do(self):
        self.bird.frame = (self.bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if get_time() - self.bird.wait_time > 3:
            self.bird.state_machine.handle_state_event(('TIMEOUT', None))

    def draw(self):
        if self.bird.face_dir == 1: # right
            self.bird.image.clip_draw(int(self.bird.frame) * 100, 300, 100, 100, self.bird.x, self.bird.y)
        else: # face_dir == -1: # left
            self.bird.image.clip_draw(int(self.bird.frame) * 100, 200, 100, 100, self.bird.x, self.bird.y)

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
        self.bird.frame = (self.bird.frame + 1) % 8
        self.bird.x += self.bird.dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        if self.bird.face_dir == 1: # right
            self.bird.image.clip_draw(self.bird.frame * 100, 100, 100, 100, self.bird.x, self.bird.y)
        else: # face_dir == -1: # left
            self.bird.image.clip_draw(self.bird.frame * 100, 0, 100, 100, self.bird.x, self.bird.y)

class Bird:
    def __init__(self):
        self.x, self.y = 400, 90
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame = 0
        self.face_dir = 1
        self.dir = 0

        self.IDLE = Idle(self)
        self.RUN = Run(self)
        self.state_machine = StateMachine(
            self.IDLE,
            {
                self.IDLE: {right_down: self.RUN, left_down: self.RUN,
                            right_up: self.RUN, left_up: self.RUN},
                self.RUN: {right_up: self.IDLE, left_up: self.IDLE, right_down: self.IDLE,
                           left_down: self.IDLE}
            }
        )

    def update(self):
        self.state_machine.update()


    def handle_event(self, event):
        self.state_machine.handle_state_event(('INPUT', event))


    def draw(self):
        self.state_machine.draw()

