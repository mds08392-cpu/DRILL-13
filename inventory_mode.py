from pico2d import *
import game_framework
import game_world

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    # play_mode 는 멈추지 않고 계속 동작한다
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    pass


def pause():
    pass


def resume():
    pass
