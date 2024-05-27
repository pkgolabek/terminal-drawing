
from drawing.layer import Layer

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.layers = {}

    def add_layer(self, name):
        if name not in self.layers:
            self.layers[name] = Layer(name, self.width, self.height)
        return self

    def __getattr__(self, name):
        if name in self.layers:
            return self.layers[name]
        raise AttributeError(f"'Canvas' object has no attribute '{name}'")

    def draw(self):
        for layer in self.layers.values():
            if layer.visible:
                layer.draw(self)
        # Assuming the buffer is a list of strings
        for row in self.buffer:
            print(''.join(row))

    def clear(self):
        self.buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]

