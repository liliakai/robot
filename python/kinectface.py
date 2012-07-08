#!/usr/bin/env python
import cv
import kinectutils as kinect
import cvutils as cvu
import controller as bot
#import freenect

# Set up for robot control. How far to the left/right must a face be
# to cause the robot to change direction? Specified as a fraction of 
# image width.
leftLimit = 0.25
rightLimit = 0.75

useDisplay = True;

if (useDisplay):
    cv.NamedWindow('Video')
    print('Press ESC in window to stop')

hc = cv.Load("/usr/share/opencv/data/haarcascade_frontalface_default.xml")
ms = cv.CreateMemStorage()
counter = 0

while True:
    video = kinect.get_video()
    width = video.width
    height = video.height

    rcenter = (width/4,height/4,width/2,height*3/4)

    bincount = 4

    mask = cv.CreateImage((width,height),8,1)
    cv.Zero (mask)
    cv.SetImageROI (mask, rcenter)
    cv.Set (mask, 1)
    cv.ResetImageROI (mask)

    cv.Rectangle(video, (width/4,height/4), (width*3/4,height), 255)

    # define our 'control region'
    xleft = int(leftLimit*width)
    xright = int(rightLimit*width)
    faces = cv.HaarDetectObjects(video, hc, ms, 1.25, 2, 0, (50,50))
    # move the robot toward the first face it sees
    for (x,y,w,h),n in faces:
        cv.Rectangle(video, (x,y), (x+w,y+h), 255)
        if x+w > xright:
        	bot.moveBot("right",50);
        	print "right"
#                sleep(0.2)
#                bot.stopBot()
        elif x < xleft:
        	bot.moveBot("left",50);
        	print "left"
#                sleep(0.2)
#                bot.stopBot()
        else:
        	bot.moveBot("right",0); # stop turning
        	bot.moveBot("left",0);
        	if max(w,h) > height/4:
        		bot.moveBot("rev",50);
        	if max(w,h) < height/7:
        		bot.moveBot("fwd",150);
        break # don't process any more faces.
    
    if (useDisplay):
        cv.ShowImage('Video', video)
    
    print ("frame " + str(counter))
    counter = counter + 1
    if cv.WaitKey(10) == 27:
        break
