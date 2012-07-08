#!/usr/bin/env python
import cv
import controller as bot
from time import sleep
##### CONFIGURATION OPTIONS #################

# Display video output?
# Set to false if running this script remotely or with no display attached.
# Script may run faster with useDisplay=False.
useDisplay = True;

# Set up for robot control. How far to the left/right must a face be
# to cause the robot to change direction? Specified as a fraction of 
# image width.
leftLimit = 0.25
rightLimit = 0.75

# What is the device number of the camera?
# ex: we use /dev/video1 (on linux), so 
# deviceNumber = 1. if you only have one camera
# plugged in, deviceNumber should probably be 0
deviceNumber = 1

##############################################

def main(argv):
    # create the window
    if (useDisplay):
        cv.NamedWindow('Video')
        print('Press ESC in window to stop')
        
    # create capture device
    capture = cv.CreateCameraCapture(deviceNumber)
    if not capture:
        print "Error opening capture device. Check deviceNumber."
        return 1

    # set up for face detection
    hc = cv.Load("/usr/share/opencv/data/haarcascade_frontalface_default.xml")
    ms = cv.CreateMemStorage()
    counter = 0

    while True:
        # capture the current frame
        video = cv.QueryFrame(capture)
        if video is None:
            break    

        width = video.width
        height = video.height

        # define our 'control region'
        xleft = int(leftLimit*width)
        xright = int(rightLimit*width)

        # detect faces
        faces = cv.HaarDetectObjects(video, hc, ms, 1.25, 2, 0, (50,50))

        # move the robot toward the first face it sees
        for (x,y,w,h),n in faces:
            cv.Rectangle(video, (x,y), (x+w,y+h), 255)
            if x+w > xright:
                bot.moveBot("right",125);
                print "right"
#                sleep(0.2)
#                bot.stopBot()
            elif x < xleft:
                bot.moveBot("left",125);
                print "left"
#                sleep(0.2)
#                bot.stopBot()
            else:
                bot.moveBot("right",0); # stop turning
                bot.moveBot("left",0);
                bot.moveBot("fwd",255);
            break # don't process any more faces.
    
        if (useDisplay):
            # draw the "control region" on the image
            cv.Rectangle(video, (xleft,0), (xright,height), 255)
            cv.ShowImage('Video', video)
    
        counter = counter + 1
        if cv.WaitKey(10) == 27:
            break

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
