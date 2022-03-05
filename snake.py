from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            pos = self.segments[seg_num-1].pos()
            self.segments[seg_num].goto(pos)
        self.segments[0].forward(MOVING_DISTANCE)