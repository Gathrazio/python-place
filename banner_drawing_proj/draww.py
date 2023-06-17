# Tenacious Guide
# Banner art with turtle

import pattern as pa
import numpy as np

def logoScale(scale_factor, parameter_vector):
    return scale_factor * parameter_vector


def yt_Logo(scale, x_loc, y_loc):
    w_width, w_height = 2048, 1152  # turtle window width and height
    offset = 12.53
    radius = 7.5
    count = 38
    color = "blue"
    starting_ang = 0
    rotation = 0
    extent = 270

    star_offset = -7.5
    width = 6.25
    height = 8.7

    params = np.array([offset, radius, count, star_offset, width, height])

    scaled_params = logoScale(scale, params)

    noffset = scaled_params[0]
    nradius = scaled_params[1]
    ncount = scaled_params[2]
    nstar_offset = scaled_params[3]
    nwidth = scaled_params[4]
    nheight = scaled_params[5]

    pa.setup(w_width, w_height)  # sets up turtle and turtle window


    pa.drawCirclePattern(x_loc, y_loc, noffset, nradius, ncount, color, extent, None, rotation, starting_ang, "cclockwise")
    pa.drawCirclePattern(x_loc, y_loc - 2 * (nradius + noffset), noffset, nradius, ncount, color, extent, None, rotation, 90, "")
    pa.drawCirclePattern(x_loc - 2 * (nradius + noffset), y_loc - 2 * (nradius + noffset), noffset, nradius, ncount, color, 90, None, rotation, 0, "cclockwise")
    pa.drawCirclePattern(x_loc - 2 * (nradius + noffset), y_loc, noffset, nradius, ncount, color, 180, None, rotation, 270, "")
    pa.drawCirclePattern(x_loc - 2 * (nradius + noffset), y_loc + 2 * (nradius + noffset), noffset, nradius, ncount, color, 90, None, rotation, 270, "cclockwise")
    pa.drawCirclePattern(x_loc, y_loc + 2 * (nradius + noffset), noffset, nradius, ncount, color, 180, None, rotation, 180, "")
    pa.drawCirclePattern(x_loc + 2 * (nradius + noffset), y_loc + 2 * (nradius + noffset), noffset, nradius, ncount, color, 90, None, rotation, 180, "cclockwise")
    pa.drawCirclePattern(x_loc + 2 * (nradius + noffset), y_loc, noffset, nradius, ncount, color, extent, None, rotation, 90, "")


    pa.drawRectanglePattern(x_loc, y_loc, nstar_offset, "teal", nwidth, nheight, np.int(ncount / 3), rotation)
    pa.drawRectanglePattern(x_loc + 2 * (nradius + noffset), y_loc, nstar_offset, "crimson", nwidth, nheight, np.int(ncount / 3), rotation)
    pa.drawRectanglePattern(x_loc, y_loc - 2 * (nradius + noffset), nstar_offset, "goldenrod", nwidth, nheight, np.int(ncount / 3), rotation)
    pa.drawRectanglePattern(x_loc, y_loc + 2 * (nradius + noffset), nstar_offset, "dim gray", nwidth, nheight, np.int(ncount / 3), rotation)
    pa.drawRectanglePattern(x_loc - 2 * (nradius + noffset), y_loc, nstar_offset, "deep sky blue", nwidth, nheight, np.int(ncount / 3), rotation)
    pa.done()


def yt_Banner():
    w_width, w_height = 2048, 1152   # turtle window width and height
    pa.setup(w_width, w_height)   # sets up turtle and turtle window


    pa.drawCirclePatternMulticolor(0, 80, 125, 70, 350, None, None, 0)
    yt_Logo(1.8, 0, 80)

    pa.drawRectanglePattern(550, -280, -80, "black", 50, 80, 70, 0)
    pa.drawRectanglePattern(-550, -280, -80, "black", 50, 80, 70, 0)
    pa.drawRectanglePattern(550, 280, -80, "black", 50, 80, 70, 0)
    pa.drawRectanglePattern(-550, 280, -80, "black", 50, 80, 70, 0)

    pa.encapsule_rect_pattern(550, -280, 50, 80, "black")
    pa.encapsule_rect_pattern(-550, -280, 50, 80, "black")
    pa.encapsule_rect_pattern(550, 280, 50, 80, "black")
    pa.encapsule_rect_pattern(-550, 280, 50, 80, "black")

    pa.drawCirclePattern(-430, 90, 15, 40, 50, "firebrick", 360, 5, 144, 0)
    pa.drawCirclePattern(430, 90, 15, 40, 50, "firebrick", 360, 5, 144, 0)
    pa.drawCirclePattern(-430, -90, 15, 40, 50, "dark turquoise", 360, 5, 144, 0)
    pa.drawCirclePattern(430, -90, 15, 40, 50, "dark turquoise", 360, 5, 144, 0)

def main():
    yt_Banner()

    pa.done()
    response = input("Press Y to close drawer: ")

    if response == "Y":
        quit()

yt_Logo(4, 0, 80)






