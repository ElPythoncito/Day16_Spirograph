# ----------------------------------------------------EL PYTHONCITO XD 🐍
from turtle import Turtle, Screen
import colorsys


def write_pythoncito(spirographx):
    spirograph.shape("turtle")
    spirographx.color("chartreuse1")
    spirographx.up()
    spirographx.left(90)
    spirographx.forward(300)
    spirographx.left(90)
    spirographx.forward(50)
    spirographx.right(90)
    spirographx.write("EL PYTHONCITO XD")
    spirographx.home()
    spirographx.down()


# ---------------------------------------------------------------- My Screen
my_screen = Screen()
my_screen.title("Day 16 Spirograph - El Pythoncito XD 🐍")
my_screen.bgcolor("black")

# --------------------------------------------------------------😉😉😉Spirograph 1
spirograph = Turtle()

write_pythoncito(spirograph)
spirograph.speed("fastest")  # Change velocity

num_colors = 18
colors = [colorsys.hsv_to_rgb(i / num_colors, 1, 1) for i in range(num_colors)]

# ----------------------------------------Draw the spirograph 1
for i in range(36):
    spirograph.color(colors[i % num_colors])
    spirograph.circle(120)
    spirograph.right(10)
    spirograph.circle(60)
    spirograph.right(10)

my_screen.clearscreen()

# ------------------------------------------------------------------ SPIROGRAPH 2
spirograph2 = Turtle()
my_screen.bgcolor("black")

write_pythoncito(spirograph2)

spirograph2.speed("fastest")

num_colors2 = 36
colors = [colorsys.hsv_to_rgb(i / num_colors2, 1, 1) for i in range(num_colors2)]

# ---------------------- Draw spirograph 2
for i in range(100):
    spirograph2.color(colors[i % num_colors2])
    spirograph2.forward(i * 2)
    spirograph2.right(59)
    spirograph2.circle(40)
my_screen.clearscreen()

# -----------------------------------------------------------------SPIROGRAPH 3
spirograph3 = Turtle()
my_screen.bgcolor("black")
write_pythoncito(spirograph3)

spirograph3.speed("fastest")

num_colors3 = 50
colors = [colorsys.hsv_to_rgb(i / num_colors3, 1, 1) for i in range(num_colors3)]

for i in range(60):
    spirograph3.color(colors[i % num_colors3])
    spirograph3.circle(120)
    spirograph3.left(10)

my_screen.clearscreen()

# ------------------------------------------------------------------SPIROGRAPH 4
spirograph4 = Turtle()
my_screen.bgcolor("black")
write_pythoncito(spirograph4)

spirograph4.speed("fastest")

num_colors4 = 50
colors = [colorsys.hsv_to_rgb(i / num_colors4,1,1) for i in range(num_colors4)]

for i in range(120):
    spirograph4.color(colors[i % num_colors4])
    spirograph4.circle(100, steps=6)
    spirograph4.right(10)
    spirograph4.forward(i * 0.05)

my_screen.exitonclick()
