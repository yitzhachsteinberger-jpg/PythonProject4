import arcade


class Key(arcade.Sprite):
    def __init__(self, center_x, center_y):
        texture = "small yellow square"
        super().__init__(texture, center_x, center_y)
        self.texture = texture
        self.center_x = center_x
        self.center_y = center_y

