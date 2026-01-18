from manim import *

class HelloWorld(Scene):
    def construct(self):
        rectangle = Rectangle()
        rectangle.set_fill(GREY_BROWN, opacity=1.5)
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        
        self.play(Transform(rectangle,circle))
        