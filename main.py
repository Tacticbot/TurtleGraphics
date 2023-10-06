import turtle as t
import random

# rgb_colours = []
# colours = colorgram.extract("image.jpg", 30)
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colours.append(new_color)

# print(rgb_colours)
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.setheading(225)
tim.forward(350)
tim.setheading(0)

n_iter = 10
while (n_iter):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    n_iter -= 1

tim.hideturtle()
screen = t.Screen()
screen.exitonclick()