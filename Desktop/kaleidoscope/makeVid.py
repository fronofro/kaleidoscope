import argparse
parser = argparse.ArgumentParser(description="Image flipper animator")
parser.add_argument('-i','--image',help='Filenam of input image')
passedIn = parser.parse_args()

from subprocess import call
import os
if not os.path.isdir('output/'):
    call(['mkdir', 'output'])

for i in range(360):
    print('Doing number %i', i)
    call(['python3', 'scaleRotate.py','-i',passedIn.image, '-o','output/'+str(i)+'.jpg','-r', str(i)])

call(['ffmpeg', '-i', 'output/%d.jpg', '-profile:v', 'high', '-level', '4.0', '-strict', '-2', 'out.mp4'])