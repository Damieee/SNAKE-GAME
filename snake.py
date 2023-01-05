from turtle import Turtle
DISTANCE=20
UP=90
LEFT=180
RIGHT=0
DOWN=270
x_coordinates=[(0,0), (-20,0), (-40,0)]


class Snake:

    def __init__(self):
        self.segments=[]
        self.create_initial_snake()
        self.head=self.segments[0]

    def create_initial_snake(self):
        for coords in x_coordinates:
            self.create_snake(coords)

    def create_snake(self, POSITION):
        #assign new segment to the snake.
        new_seg=Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(POSITION)
        self.segments.append(new_seg)

    def extend(self):
        self.create_snake(self.segments[-1].position())
            
    def move_snake(self):
        for segs in range(len(self.segments)-1, 0, -1):
            new_x_coordinate = self.segments[segs-1].xcor()
            new_y_coordinate = self.segments[segs-1].ycor()
            self.segments[segs].goto(new_x_coordinate, new_y_coordinate)
        self.head.forward(DISTANCE)

    def reset(self):
        for segs in self.segments:
            segs.goto(2000,2000)
        self.segments.clear()
        self.create_initial_snake()
        self.head=self.segments[0]

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
