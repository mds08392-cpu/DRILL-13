from pico2d import *
import game_framework
import game_world

image = None

# 키 -> (공 크기, 출력 메세지)
ITEMS = {
    SDLK_0: (0, '공 삭제'),
    SDLK_1: (21, '작은공'),
    SDLK_2: (42, '큰공'),
}


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
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key in ITEMS:
            import play_mode
            size, message = ITEMS[event.key]
            play_mode.boy.ball_size = size
            print(message)
            game_framework.pop_mode()


def pause():
    pass


def resume():
    pass
