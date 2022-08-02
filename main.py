import colorgram
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)


def colour_list_gen(n_colours, image):
    colour_list = []
    colours = colorgram.extract(image, n_colours)
    for number in range(1, n_colours):
        colour_list.append((colours[number].rgb[0], colours[number].rgb[1], colours[number].rgb[2]))
    return colour_list


colour_list = colour_list_gen(8, "slave_knight_gael_boss.jpeg")

tim = Turtle()
tim.shape("circle")
tim.color("black")


def print_circle():
    tim.speed(0)
    colour_pick = colour_list[randint(0, len(colour_list) - 1)]
    tim.pencolor(255, 255, 255)
    tim.fillcolor(colour_pick)
    tim.pendown()
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()
    tim.penup()


def print_grid(x, y, spacing):
    tim.hideturtle()
    x_cor = 0
    y_cor = 0
    for number_1 in range(1, y):
        for number_2 in range(1, x):
            print_circle()
            tim.forward(spacing)
        x_cor = 0
        y_cor += spacing
        tim.setpos(x_cor, y_cor)


print_grid(10, 10, 30)

screen.exitonclick()
