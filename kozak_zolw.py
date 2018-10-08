import turtle



def main():
    wn = turtle.Screen()  # creates a graphics window
    alex = turtle.Turtle()  # create a turtle named alex

    def triangle(lenght):
        for i in range(3):
            alex.forward(lenght)
            alex.left(120)

    for i in range(36):
        triangle(100)
        alex.right(10)


    turtle.exitonclick()

if __name__ == "__main__":
    main()

