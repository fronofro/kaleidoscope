import PIL
from PIL import Image, ImageOps
from math import pi
from math import sqrt
from math import radians
from math import sin
from math import cos
import pygame
pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

import argparse
parser = argparse.ArgumentParser(description="Image scale rotater")
parser.add_argument('-i','--image',help='Filename of input image',required=True)
parser.add_argument('-o','--output',help='output file', default='output.jpg', required=True)
parser.add_argument('-r','--rotate',help='degrees of rotation', default='5', required=True)
passedIn = parser.parse_args()

# First, let's load and then copy our input image
newImage = pygame.image.load(passedIn.image)
blankImage = newImage.copy()

# Next, let's make sure they're both 'RGBA', so parts can be invisible
newImage = newImage.convert_alpha()
blankImage = blankImage.convert_alpha()

# Finally, let's make sure we know how big our image is
imageWidth = newImage.get_width()
imageHeight = newImage.get_height()

def rotatePoint(x1, y1, x2, y2, rotate):
    '''
    Rotates around x1, y2 by rotate degrees
    '''
    inRadians = radians(rotate)
    nx = cos(inRadians) * (x1 - x2) - sin(inRadians) * (y1 - y2) + x2
    ny = sin(inRadians) * (x1 - x2) + cos(inRadians) * (y1 - y2) + y2
    return int(nx), int(ny)

scaler = 10
rotate = float(passedIn.rotate)
for i in range(20):
    scaled = pygame.transform.scale(newImage, [int(imageWidth - sqrt(scaler)), int(imageHeight - sqrt(imageHeight))])
    blankImage.blit(pygame.transform.rotate(scaled, sqrt(pi * rotate / 180)), rotatePoint(scaler, scaler, imageWidth // 2, imageHeight // 2, sqrt(rotate)))
    scaler += 2
    rotate += rotate

pygame.image.save(blankImage, passedIn.output)

# create a new surface, twice as big in each dimension
doubleOut = pygame.Surface((imageWidth * 2, imageHeight * 2))
# copy the above image to the top left corner
doubleOut.blit(blankImage, (0,0))
# copy a flipped image to the center top corner
doubleOut.blit(pygame.transform.flip(blankImage, True, False), (imageWidth, 0))
# copy a flipped rotated image to the bottom left corner
doubleOut.blit(pygame.transform.flip(pygame.transform.rotate(blankImage, 180), True, False), (0, imageHeight))
# copy a rotated image to the bottom middle corner
doubleOut.blit(pygame.transform.rotate(blankImage, 180), (imageWidth, imageHeight))
# save it with the word 'mirror_' in front of the file name passed in
pygame.image.save(doubleOut, passedIn.output)