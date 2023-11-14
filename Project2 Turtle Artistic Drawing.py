import turtle

sc = turtle.Screen()
sc.bgcolor("black")

# Create the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")

# Create the planet
mercury = turtle.Turtle()
mercury.shape("circle")
mercury.color("brown")
mercury.penup()
mercury.goto(0, -50)  # Place Mercury at an initial position

venus = turtle.Turtle()
venus.shape("circle")
venus.color("maroon")
venus.penup()
venus.goto(0, -100)  # Place Venus at an initial position

earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.penup()
earth.goto(0, -150)  # Place Earth at an initial position

mars = turtle.Turtle()
mars.shape("circle")
mars.color("red")
mars.penup()
mars.goto(0, -200)  # Place Mars at an initial position

jupiter = turtle.Turtle()
jupiter.shape("circle")
jupiter.color("orange")
jupiter.penup()
jupiter.goto(0, -250)  # Place Jupiter at an initial position

saturn = turtle.Turtle()
saturn.shape("circle")
saturn.color("white")
saturn.penup()
saturn.goto(0, -300)  # Place Saturn at an initial position

uranus = turtle.Turtle()
uranus.shape("circle")
uranus.color("green")
uranus.penup()
uranus.goto(0, -350)  # Place Uranus at an initial position

neptune = turtle.Turtle()
neptune.shape("circle")
neptune.color("purple")
neptune.penup()
neptune.goto(0, -400)  # Place Neptune at an initial position

# Define the radius of the circular path
radius = 50

# Modify the last for loop to make the planets revolve around the sun
for planet in [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]:
    planet.pendown()
    planet.circle(radius)
    radius += 50  # Increase the radius for each planet

# Close the turtle graphics window when done
sc.exitonclick()
