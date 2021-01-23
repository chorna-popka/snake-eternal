from turtle import Turtle
from gradient import gradient

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
PIECES = 3


class Snake:
    def __init__(self, color):
        self.color = color
        self.shape = "square"
        self.pieces = [ ]
        self.create_snake()
        self.head = self.pieces[ 0 ]

    def create_snake(self):
        for i in range(PIECES):
            pos = (0 - 20 * i, 0)
            self.add_piece(pos)

    def add_piece(self, pos):
        t = Turtle(shape=self.shape)
        t.color(self.color)
        t.up()
        t.setpos(pos)
        self.pieces.append(t)

    def extend(self):
        self.add_piece((self.pieces[ -1 ].xcor() - 20, self.pieces[ -1 ].ycor()))
        self.update_color()

    def update_color(self):
        index = len(self.pieces) - PIECES
        if index >= len(gradient):
            # do not update color, max reached
            return

        hex_color = "#" + gradient[index]
        self.color = hex_color
        for p in self.pieces:
            p.color(hex_color)

    def move(self, speed):
        for piece_num in range(len(self.pieces) - 1, 0, -1):
            new_x = self.pieces[ piece_num - 1 ].xcor()
            new_y = self.pieces[ piece_num - 1 ].ycor()
            self.pieces[ piece_num ].goto(new_x, new_y)
        self.pieces[ 0 ].forward(speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
