from pico2d import open_canvas, delay, clear_canvas
import game_framework

import play_mode as start_mode

open_canvas(1600, 600)
game_framework.run(start_mode)
clear_canvas()