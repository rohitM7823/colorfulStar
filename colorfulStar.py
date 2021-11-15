import turtle


def start_animation():
    r = turtle.Turtle()

    r.pendown()
    r.setpos(-80, -90)
    r.pos()

    r.screen.bgcolor("black")
    r.shape("turtle")
    color_list = ["red", "cyan", "#98EE90", "white"]
    r.shape("turtle")
    r.color("white")
    r.speed(10)
    i = 0
    for x in range(51):
        if i != 4:
            r.color(color_list[i], color_list[i])
            i += 1
            r.forward(x * 10)
            for y in range(8):
                r.right(35)
                r.forward(40)
                r.left(70)
                r.back(i + 51)
            r.right(135)

        else:
            i = 0
            r.color(color_list[i], color_list[i])
            r.forward(x * 10)
            for y in range(8):
                r.right(35)
                r.forward(40)
                r.left(70)
                r.back(i + 51)
            r.right(135)
    r.done()


if __name__ == "__main__":
    start_animation()

