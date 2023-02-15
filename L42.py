#Emily Nixon
import turtle
jack = turtle.Turtle()
jack.color("black")
for side in range(4):
    if side == 1:
        jack.color ("red")
    if side == 2:
        jack.color ("purple")
    if side == 3:
        jack.color ("pink")
    jack.forward (100)
    jack.right (90)
