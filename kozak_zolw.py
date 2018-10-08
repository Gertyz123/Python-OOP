import turtle



def main():
    wn = turtle.Screen()  # creates a graphics window
    alex = turtle.Turtle()  # create a turtle named alex

    def triangle():
        for i in range(3):
            alex.forward(100)
            alex.left(120)

    triangle()

    turtle.exitonclick()

if __name__ == "__main__":
    main()

