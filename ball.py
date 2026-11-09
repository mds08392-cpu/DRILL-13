from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None
    small_image = None

    def __init__(self, x, y, velocity, size=21):
        if Ball.image is None:
            Ball.image = load_image('ball41x41.png')
        if Ball.small_image is None:
            Ball.small_image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.velocity = velocity
        self.size = size

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        if self.size == 21:
            self.small_image.draw(self.x, self.y, 21, 21)
        else:
            self.image.draw(self.x, self.y, 42, 42)
