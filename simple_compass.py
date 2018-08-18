# Simple compass. Should always point north

from microbit import *

if not compass.is_calibrated():
    compass.calibrate()
    
while True:
    dir = ((360-compass.heading())/360)*12
    display.show(Image.ALL_CLOCKS[int(dir)])
    sleep(200)