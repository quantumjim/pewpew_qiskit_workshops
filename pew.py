'''
Copyright IBM 2019. This code is licensed under the Apache License, Version 2.0.
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import time

K_X = 0x01
K_DOWN = 0x02
K_LEFT = 0x04
K_RIGHT = 0x08
K_UP = 0x10
K_O = 0x20

B_X = 'x'
B_DOWN = 'd'
B_LEFT = 'l'
B_RIGHT = 'r'
B_UP = 'u'
B_O = 'o'

with open('input.txt','r') as file:
    input_num = len(file.read())

def init():
    global fig, ax

    fig = plt.figure(figsize=(8,8),facecolor=(1,1,1))
    ax = fig.gca()
    plt.axis('off')
    fig.show()

def show(pix):
    for Y in range(8):
        for X in range(8):
            ax.add_patch( Rectangle( (X/8,7/8-Y/8), 1/8, 1/8, color=(int(pix.pixel(X,Y))/3,0,0)) ) 
    fig.canvas.draw()

def keys():
    global input_num
    with open('input.txt','r') as file:
        inputs = file.read()
        new_input_num = len(inputs)
    if new_input_num>input_num:
        keys = inputs[-1]
        input_num = new_input_num
    else:
        keys = 0x00
    for b,k in [(B_UP,K_UP),(B_DOWN,K_DOWN),(B_LEFT,K_LEFT),(B_RIGHT,K_RIGHT),(B_X,K_X),(B_O,K_O)]:
        if keys==b:
            print('key press:',b)
            return k
    return 0x00

def tick(delay):
    time.sleep(delay)
    
class Pix:
    def __init__(self):
        self.buffer = [[0 for x in range(8)] for y in range(8)]
        
    def pixel(self, x, y, color=None):
        if color is None:
            return self.buffer[y][x]
        else:
            self.buffer[y][x] = color