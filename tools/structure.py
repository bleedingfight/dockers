from manimlib import *

class InteractiveDevelopment(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.set_stroke(BLUE_E, width=10,height=)
        
        text = Text("welcome to dockers")
        self.add(text)
        self.play(ShowCreation(text))
        self.wait()
        self.play(ShowCreation(square))
