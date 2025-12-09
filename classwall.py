import arcade

class Wall (arcade.Sprite):
    def __init__(self, texture, center_x, center_y ):

        super().__init__(texture, center_x, center_y)
