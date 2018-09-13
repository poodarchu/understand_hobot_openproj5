import numpy as np
from enum import Enum, unique

IMAGE_WIDTH = 1280
IMAGE_HEIGHT = 720


@unique
class Modes(Enum):
    LeftRight = 1
    LeftMiddleRight = 2
    LTRB = 3
    TopDown = 4

for name, member in Modes.__members__.items():
    print(name, '=>', member, ',', member.value)

def lr_func(ele):
    mid = (ele[0] + ele[2])/2.
    return mid

def lmr_func(ele):
    return ele[0]

def td_func(ele):
    return ele[1]

def snap2grid(objects, mode=Modes.LeftRight):

    if mode == Modes.LeftRight:
        x = np.linspace(0, IMAGE_WIDTH, num=3)
        y = np.linspace(0, IMAGE_HEIGHT, num=2)
        xv, yv = np.meshgrid(x, y, sparse=False, indexing='ij')

        # for cls, locations in objects.iteritems():
        objects.sort(key=lr_func)

        return objects


    elif mode == Modes.LeftMiddleRight:
        x = np.linspace(0, IMAGE_WIDTH, num=4)
        y = np.linspace(0, IMAGE_HEIGHT, num=2)

        return objects
    elif mode == Modes.LTRB:
        x = np.linspace(0, IMAGE_WIDTH, num=3)
        y = np.linspace(0, IMAGE_HEIGHT, num=3)

        return objects
    else:
        x = np.linspace(0, IMAGE_WIDTH, num=2)
        y = np.linspace(0, IMAGE_HEIGHT, num=3)

        return objects
