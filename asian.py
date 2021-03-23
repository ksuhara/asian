# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480

# tells how many times to iterate through the following mechanism
# which equals the number of birds
# e.g. 
# for x in range(0-200) 
# would generate 201 birds numbered 0-200
for x in range(0, 50):

    # using ETH block number as starting random number seed
    b=11981207
    seed(x+b)

    #head color - randomly generate each number in an RGB color
    hd = (randint(0, 256), randint(0, 256), randint(0, 256))
    c=randint(0,500)
    seed(c)

    #throat color - same as head color
    th = (randint(0, 256), randint(0, 256), randint(0, 256))
    d = randint(0,1000)
    seed(d)

    #eye "white" color
    # if random number between 1-1000 is 47 or less - Crazy Eyes!
    if d > 47:
        # normal eyes are always the same color
        ew = (240,248,255)
        ey = (0, 0, 0)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
        ew = (randint(0, 256), randint(0, 256), randint(0, 256))
        ey = (154, 0, 0)
    e = randint(0,1000)
    seed(e)

    # face color
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> 肌色1
        fb = (255, 241, 223)
        fbr = 255

    elif 500 >= f > 47:
        fb = (247, 221, 195)
        fbr = 247
    else:
        fb = (104, 78, 52)
        fbr = 104

    # face basic 顔の色

    # face dark 顔の影
    fd = (fbr - 25, fbr - 45, fbr - 65)

    # hair basic 髪の毛の色
    hbr = randint(0, 225)
    hbb = randint(0, 225)
    hbg = randint(0, 225)
    hb = (hbr, hbb, hbg)

    #hair light
    hl = (hbr + 30, hbb + 30, hbg + 30)

    # mouth
    mo = (randint(0, 256), randint(0, 256), randint(0, 256))

    # background color
    bg = (238, 238, 238)
    # outline color
    ol = (0, 0, 0)

    basic_bird = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, fb, fb, fb, fb, fb, fb, ol, ol, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fd, fd, fb, fb, fb, fb, fb, fb, fd, fd, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, ol, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, ol, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, mo, mo, mo, mo, mo, mo, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, mo, mo, mo, mo, mo, mo, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]        
    ]

    afroHead = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, ol, ol, ol, fb, fb, fb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, ol, ol, hb, fb, fb, fb, fb, fb, fb, fb, fd, fd, fd, fb, fb, fb, fd, fd, fd, fb, fb, fb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, ol, fb, fd, fd, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, ol, fb, fb, fb, fd, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, fb, fb, fb, ol, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, ol, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    ]

    bottom = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, mo, mo, mo, mo, mo, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fd, fd, fd, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fd, fd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg] 
    ]

    woodpecker = np.concatenate([afroHead, bottom])

    jay = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hl, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, ol, ol, ol, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, ol, ol, hb, fb, fb, fb, fb, fb, fb, fb, fd, fd, fd, fb, fb, fb, fd, fd, fd, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, ol, fb, fd, fd, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, ol, fb, fb, fb, fd, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, fb, fb, fb, ol, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, ol, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, fb, fb, fb, ol, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, hb, bg, hb, hb, hb, hb, hb, hb, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, hb, hb, bg, hb, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, bg, hb, hb, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, mo, mo, mo, mo, mo, fb, fb, fb, fb, fb, ol, bg, hb, bg, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hb, bg, bg, hb, hb, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, bg, hb, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fd, fd, fd, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fd, fd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg] 
    ]

    eagle = [
         [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hl, hl, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, hb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hb, hb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, ol, ol, ol, fb, fb, fb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hb, fb, fb, fb, fb, fb, fb, fb, fd, fd, fd, fb, fb, fb, fd, fd, fd, fb, fb, fb, hb, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fb, fd, fd, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fb, fb, fb, fd, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, ol, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, mo, mo, mo, mo, mo, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fd, fd, fd, fb, fb, fb, fb, fb, fb, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fd, fd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, fb, fb, fb, fb, fb, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]  
    ]

    # choose which bird image to use
    seed(f)
    g = randint(0,1000)
    if g > 250:
        # if random number is 251 - 1000 >> basic bird
        pixels = basic_bird
        p = "basic"
    elif 250 >= g > 100:
        # 101 - 250 >> jay
        pixels = jay
        p = "jay"
    elif 100 >= g > 40:
        # 41 - 100 >> woodpecker
        pixels = woodpecker
        p = "pecker"
    elif 40 >= g > 5:
        # 6 - 40 >> eagle
        pixels = basic_bird
        p = "eagle"
    else:
        # if random number is 5 or less >> cockatoo!!
        pixels = basic_bird
        p = "cockatoo"

    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = '/Users/kentasuhara/devs/generate-bitbirds' + '/bird_images/' + (str(x)) + '.png'
    new_image.save(imgname)