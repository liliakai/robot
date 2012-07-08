import time
import pygame
from pygame import locals
import Pyro.core

pygame.init()
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()

numaxes = joy.get_numaxes()
numbuts = joy.get_numbuttons()
numhats = joy.get_numhats()
print("Found joystick: %s" % joy.get_name())
print("%d axes %d buttons %d hat" % (numaxes,numbuts,numhats))

remote = Pyro.core.getProxyForURI("PYROLOC://75.101.62.93:7766/joystick")
print "pyro connected"

last = time.time()
tsum = 0
tcnt = 0
while 1:
        pygame.event.get()
        x = joy.get_axis(0)
        y = joy.get_axis(1)
        z = joy.get_axis(2)
        th = joy.get_axis(3)
        buttons = map(joy.get_button,range(numbuts))
        hat = joy.get_hat(0)
        remote.update(x,y,z,th,buttons,hat)

        #if (x or y or z or th or any(buttons) or any(hat)):
        #remote.update(0,0,0,0,[0,0,0,0,0,0,0,0],(0,0))
        now = time.time()
        tsum += now-last
        tcnt = tcnt+1
        last = now

        if tcnt == 100:
            #print tsum / tcnt
            tcnt = 0
            tsum = 0
            print([x,y,z,th,buttons,hat])
        


