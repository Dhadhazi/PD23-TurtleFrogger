from turtle import Turtle

class Car(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.goto(300, position)
        self.setheading(180)

    def move(self, distance):
        self.forward(distance)