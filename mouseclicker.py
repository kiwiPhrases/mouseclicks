import pyautogui as gui
import numpy as np
import time
import sys


def mouseclick(minutes, max_pixel_error=200, max_click_sleep=10):
    """
    Clicks the mouse around the center of the screen for user-given minutes
    There is some randomness to the mouse click location and click interval
    Arguments:
        minutes: number of minutes to click for
        max_pixel_error (optional, default=100): max distance from screen center around which to click
        max_click_sleep (optional, default=15): max number of seconds between clicks.
    """
    # get screen size for navigation
    x = gui.size().width
    y = gui.size().height 
    
    

    # compute seconds
    timegap = minutes*60

    # get current time
    starttime = time.time()
    endtime = starttime+timegap

    print("Starting clicks for %.2f minutes" %minutes)
    i = 0
    # keep looping until minutes run down
    while time.time()<endtime: 
        
        # give a bit of randomness to the click
        err = np.random.randint(0,max_pixel_error,size=2)

        # click
        gui.click(x/2+err[0],y/2+err[1])
        
        # pause
        time.sleep(np.random.randint(0,max_click_sleep))
        i=+1
    
    print("Clicks terminated. %d clicks supplied" %i)

if __name__ == '__main__':
    mouseclick(sys.arg[1])