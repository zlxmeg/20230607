from microbit import *
import neopixel

np=neopixel.NeoPixel(pin12,8)

np[1]=(225,225,225)
np[2]=(225,225,225)
np[5]=(225,0,0)
np[6]=(225,0,0)

def left_on():
    np[3]=(255,100,0)
    np[4]=(255,100,0)
    np.show()
def left_off():
    np[3]=(0,0,0)
    np[4]=(0,0,0)
    np.show()

def right_on():
    np[0]=(255,100,0)
    np[7]=(255,100,0)
    np.show()
def right_off():
    np[0]=(0,0,0)
    np[7]=(0,0,0)
    np.show()

while True:
    right_on()
    left_on()
    sleep(300)


