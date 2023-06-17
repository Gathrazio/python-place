# Noah Jensen
# CS 1400 -- 001
# Assn 11

import turtle
import random
import numpy as np

tr = turtle.Turtle()  # creating the turtle object

tr.hideturtle() # hide the turtle
tr.width(4)

# defining the setup function, which determines the dimensions of the window, the speed of turtle, and keeps turtle
# from drawing
def setup(width, height):
    turtle.setup(width, height)
    # *Note: I am being given an "Cannot find reference in 'turtle.py'" error for this method; which is odd because
    # I saw Dr. Mano use this function in this manner and everything worked fine. I haven't solved this error here
    # because while the error itself exists, the program is able to run without interruption. I initially thought that
    # my version of python or pycharm was bad (thanks to some online advice), so I reinstalled both. Still no luck in
    # resolving this error. I checked the documentation beforehand and it said that the method 'setup' is actually a
    # Screen class method, yet using a different object doesn't help the original error go away. It hasn't stopped me
    # from actually doing anything; it's just annoying. Oh well.
    tr.speed(0)
    tr.color("blue")
    tr.penup()

def turtColorModeChangeRGB():
    turtle.colormode(225)


# defining the reset() function, which clears all drawings from the window and resets the speed and penup of turtle
def reset():
    tr.reset()
    tr.speed(0)
    tr.penup()


def drawRectangleMulticolorPattern(startX, startY, offset, width, height, count, rotation):
    # the parameters it takes are the position of the center of the pattern, the dimensions of the rectangles to be
    # drawn, the number of rectangles to be drawn in 360 degrees, and the rotation of each rectangle.

    spacing = 360 / count # spacing is used to determine how the angle of turtle should change after each rectangle
    tr.goto(startX, startY) # making turtle go to the position of the center of the pattern

    previous_color = "blue"

    # this for-loop executes and alignment of turtle and the drawing of each rectangle. This loop will iterate
    # 'count' number of times
    for i in range(0, count):
        previous_color = setRandomColor(previous_color)
        tr.color(previous_color) # setting the color of turtle to something random (this happens every rectangle)
        tr.goto(startX, startY)
        # telling turtle to go to the center of the pattern. This happens every time a rectangle is printed.

        tr.setheading(i * spacing)
        # setting turtle's heading to the correct angle for each rectangle to be printed equally spaced in a span of
        # 360 degrees.

        # this next bit of code is concise and efficient. It handles the case of negative offset precisely in the way
        # it should.

        if offset < 0: # the case that offset has been entered negative
            tr.backward(abs(offset)) # turtle should go backwards the magnitude of offset
        else: # if offset is not less than zero; positive or zero
            tr.forward(offset) # turtle should go forward a distance of offset
        tr.setheading(i * spacing - rotation)
        # orienting turtle correctly; if rotation is positive, turtle will tilt down rotation degrees from its
        # radius axis; if rotation is negative, turtle will tilt up in the same manner.

        tr.pendown() # turtle puts its pen down
        drawRectangle(height, width) # calling drawRectangle, which draws a single rectangle
        tr.penup() # stopping turtle from drawing as it moves back to the center of the pattern for the next iteration
        tr.setheading(0)

# defining the drawRectanglePattern() function. This will draw the rectangle pattern.
def drawRectanglePattern(startX, startY, offset, color, width, height, count, rotation):
    tr.width(3)
    # the parameters it takes are the position of the center of the pattern, the dimensions of the rectangles to be
    # drawn, the number of rectangles to be drawn in 360 degrees, and the rotation of each rectangle.

    spacing = 360 / count # spacing is used to determine how the angle of turtle should change after each rectangle
    tr.goto(startX, startY) # making turtle go to the position of the center of the pattern

    tr.color(color)  # setting the color of turtle to something random (this happens every rectangle)

    # this for-loop executes and alignment of turtle and the drawing of each rectangle. This loop will iterate
    # 'count' number of times
    for i in range(0, count):
        tr.goto(startX, startY)
        # telling turtle to go to the center of the pattern. This happens every time a rectangle is printed.

        tr.setheading(i * spacing)
        # setting turtle's heading to the correct angle for each rectangle to be printed equally spaced in a span of
        # 360 degrees.

        # this next bit of code is concise and efficient. It handles the case of negative offset precisely in the way
        # it should.

        if offset < 0: # the case that offset has been entered negative
            tr.backward(abs(offset)) # turtle should go backwards the magnitude of offset
        else: # if offset is not less than zero; positive or zero
            tr.forward(offset) # turtle should go forward a distance of offset
        tr.setheading(i * spacing - rotation)
        # orienting turtle correctly; if rotation is positive, turtle will tilt down rotation degrees from its
        # radius axis; if rotation is negative, turtle will tilt up in the same manner.

        tr.pendown() # turtle puts its pen down
        drawRectangle(height, width) # calling drawRectangle, which draws a single rectangle
        tr.penup() # stopping turtle from drawing as it moves back to the center of the pattern for the next iteration
        tr.setheading(0)


# defining the drawRectangle() function, which draws a single rectangle
def drawRectangle(height, width): # takes height and width parameters for the rectangle
    tr.pendown()
    tr.begin_fill()
    for i in range(0, 4): # will iterate four times, twice will i % 2 be 1 and twice will i % 2 be 0.
        if i % 2 == 0:
            tr.forward(height) # first, turtle draws forward a distance of height
        else:
            tr.forward(width)
        tr.left(90) # turns left after each distance decision (sans the last iteration, when i = 3
    tr.end_fill()

def encapsule_rect_pattern(x, y, height, width, color):
    tr.color(color)
    radius = np.sqrt(height ** 2 + width ** 2)
    tr.goto(x, y - radius)
    drawCircle(radius, None, None)
    tr.penup()

# defining the drawCirclePattern function, which draws a circle pattern
def drawCirclePatternMulticolor(startX, startY, offset, radius, count, extent, steps, rotation):
    # this function takes in a pattern origin, an offset, a radius (of each circle), and a count (the number of circles
    # to be drawn for each pattern in the 360 degree space around the center).

    spacing = 360 / count
    # spacing is used to delineate how the angle of turtle should change after each circle is drawn

    tr.goto(startX, startY) # telling turtle to go to the origin of the pattern

    previous_color = "blue"

    # this for-loop draws the pattern. It will iterate 'count' times
    for i in range(0, count):
        previous_color = setRandomColor(previous_color)
        tr.color(previous_color) # setting turtle to a random color each time a circle is drawn
        tr.goto(startX, startY) # telling turtle to go the the pattern origin after every time a circle is drawn
        tr.setheading(i * spacing) # turtle will orient itself at the center of the pattern in a unique line
        if offset < 0: # the case when offset is negative
            tr.backward(abs(offset)) # telling turtle to go backwards the magnitude of offset
        else:
            tr.forward(abs(offset)) # if offset is not negative, turtle should instead go forward a distance of offset
        tr.right(90 - rotation) # turtle turns right to be able to draw the circle
        tr.pendown() # turtle puts down its pen
        drawCircle(radius, extent, steps) # calling drawCircle() to draw the circle with radius 'radius'
        tr.penup() # turtle should stop drawing, ready to move back to the center and be oriented for another circle

def drawCirclePattern(startX, startY, offset, radius, count, color, extent, steps, rotation, pattern_start_ang, draw_direction):
    # this function takes in a pattern origin, an offset, a radius (of each circle), and a count (the number of circles
    # to be drawn for each pattern in the 360 degree space around the center).

    spacing = 360 / count
    # spacing is used to delineate how the angle of turtle should change after each circle is drawn

    tr.goto(startX, startY) # telling turtle to go to the origin of the pattern

    tr.color(color)  # setting turtle to desired color

    # this for-loop draws the pattern. It will iterate 'count' times
    if draw_direction == "cclockwise":
        for i in range(0, int(np.floor(count * (extent / 360))) + 1):
            tr.goto(startX, startY) # telling turtle to go the the pattern origin after every time a circle is drawn
            tr.setheading(pattern_start_ang + i * spacing) # turtle will orient itself at the center of the pattern in a unique line
            if offset < 0: # the case when offset is negative
                tr.backward(abs(offset)) # telling turtle to go backwards the magnitude of offset
            else:
                tr.forward(abs(offset)) # if offset is not negative, turtle should instead go forward a distance of offset
            tr.right(90 - rotation) # turtle turns right to be able to draw the circle
            tr.pendown() # turtle puts down its pen
            drawCircle(radius, None, steps) # calling drawCircle() to draw the circle with radius 'radius'
            tr.penup() # turtle should stop drawing, ready to move back to the center and be oriented for another circle
    else:
        for i in range(0, int(np.floor(count * (extent / 360))) + 1):
            tr.goto(startX, startY) # telling turtle to go the the pattern origin after every time a circle is drawn
            tr.setheading(pattern_start_ang - i * spacing) # turtle will orient itself at the center of the pattern in a unique line
            if offset < 0: # the case when offset is negative
                tr.backward(abs(offset)) # telling turtle to go backwards the magnitude of offset
            else:
                tr.forward(abs(offset)) # if offset is not negative, turtle should instead go forward a distance of offset
            tr.right(90 - rotation) # turtle turns right to be able to draw the circle
            tr.pendown() # turtle puts down its pen
            drawCircle(radius, None, steps) # calling drawCircle() to draw the circle with radius 'radius'
            tr.penup() # turtle should stop drawing, ready to move back to the center and be oriented for another circle

# definition of drawCircle(), which literally just calls the circle() function to draw the circle.
def drawCircle(radius, extent, steps):
    tr.pendown()
    tr.circle(radius, extent, steps)

def turtleTravel(x, y):
    tr.goto(x, y)


# definition of drawSuperPattern, which randomizes which type of pattern (circle or rectangle) and the dimensions of
# each respective shape as part of the pattern. The random variables used to represent the function parameters are
# fairly self-evident.
def drawSuperPattern(number=4):
    for i in range(1, number + 1): # for each number of patterns that will be drawn, this process should be done

        # determine the random values that both drawCirclePattern and drawRectanglePattern use (this is mostly to save
        # space in the if-else statement to follow. The exact values I used to determine their random values come from
        # the dimensions of the viewing window; I don't want the shapes to be able to spawn on the edge of the window,
        # so I've give the center dimensions a range 50 pixels from each wall. Also, I've given offset and count
        # reasonable values as well. I use randPattern to determine which pattern I will actually be drawing.
        randStartX = random.randint(-450, 450)
        randStartY = random.randint(-350, 350)
        randOffset = random.randint(-100, 100)
        randCount = random.randint(2, 60)
        randPattern = random.randint(0, 1)
        if randPattern == 0:
            # if randPattern happens to be 0, a circle pattern with the rest of the dimensions determined inside this if
            # statement will be drawn.
            randRadius = random.randint(20, 150)
            drawCirclePattern(randStartX, randStartY, randOffset, randRadius, randCount)
        else:
            # if randPattern happens to be 1, the same goes (the rest of the necessary dimensions are calculated
            # inside the statement) and a rectangle pattern will be drawn.
            randWidth = random.randint(10, 150)
            randHeight = random.randint(10, 200)
            randRotation = random.randint(-60, 60)
            drawRectanglePattern(randStartX, randStartY, randOffset, randWidth, randHeight, randCount, randRotation)


# definition of the random color function setRandomColor. I've set this function to use a randomly generated number to
# choose a color; I've implemented four options because their combination look nicest to the eye.
def setRandomColor(previous_color):
    num = random.randint(0, 6)
    # generate random number either 0, 1, 2, or 3. Whatever it is will be caught by an if case.
    if num == 0:
        if previous_color != "violet red":
            return "violet red"
        else:
            return setRandomColor(previous_color)
    elif num == 1:
        if previous_color != "blue":
            return "blue"
        else:
            return setRandomColor(previous_color)
    elif num == 2:
        if previous_color != "medium aquamarine":
            return "medium aquamarine"
        else:
            return setRandomColor(previous_color)
    elif num == 3:
        if previous_color != "crimson":
            return "crimson"
        else:
            return setRandomColor(previous_color)
    elif num == 4:
        if previous_color != "medium blue":
            return "medium blue"
        else:
            return setRandomColor(previous_color)
    elif num == 5:
        if previous_color != "black":
            return "black"
        else:
            return setRandomColor(previous_color)
    else:
        if previous_color != "purple":
            return "purple"
        else:
            return setRandomColor(previous_color)


# definition of the done() function; the instructions for this function are sparse, besides its name. I have created it
# so that turtle will be hidden and the window won't get deleted as soon as the program finishes. The window will have
# to be closed manually or the program force-quitted if the program is to be restarted.
def done():
    tr.hideturtle()
    turtle.done()

def backgroundColor(color):
    turtle.bgcolor(color)

