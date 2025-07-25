
from manim import *

class MyAxes(Axes):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add(self.create_labels())

    def create_labels(self):
        x_label = MathTex("x").next_to(self.x_axis.get_end(), RIGHT)
        y_label = MathTex("y").next_to(self.y_axis.get_end(), UP)
        return VGroup(x_label, y_label)
