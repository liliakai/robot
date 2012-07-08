#!/usr/bin/python
import time
import Pyro.core
import controller
import rockets

class JoystickController:
	def __init__(self):
#		self.x = 0
#		self.y = 0
#		self.z = 0
#		self.throttle = 0
#		self.buttons = []
#		self.hat = 0

		self.minx = 0.3
		self.miny = 0.3
		self.minz = 0.3

		self.tsum = 0
		self.tcnt = 0
		self.last = time.time()
	def update(self,x,y,z,throttle,buttons,hat):
#                self.x = x
#                self.y = y
#                self.z = z
#                self.throttle = throttle
#                self.buttons = buttons
#                self.hat = hat

		now = time.time()
		self.tcnt = self.tcnt+1
		self.tsum += now - self.last
		if self.tcnt == 100:
			#print self.tsum/self.tcnt
			self.tcnt=0
			self.tsum=0
		self.last = now

		if (abs(x) > self.minx):
			if (x > 0):
				controller.moveBot("right",int(x*255/2))
			else:
				controller.moveBot("left",abs(int(x*255/2)))
		else:
			controller.moveBot("right",0)

                if (abs(y) > self.miny):
                        if (y > 0):
                                controller.moveBot("rev",int(y*255))
                        else:
                                controller.moveBot("fwd",abs(int(y*255)))
		else:
			controller.moveBot("fwd",0)

		if (buttons[0]):
			rockets.fire()
		if (buttons[3]):
			rockets.laser()
		if (hat[1] > 0):
			rockets.up()
		if (hat[1] < 0):
			rockets.down()
                if (hat[0] > 0):
                        rockets.right()
                if (hat[0] < 0):
                        rockets.left()
	

class JoystickListener(Pyro.core.ObjBase, JoystickController):
	def __init__(self):
		Pyro.core.ObjBase.__init__(self)
		JoystickController.__init__(self)

if __name__ == "__main__":

	Pyro.core.initServer()
	daemon = Pyro.core.Daemon()
	joy = JoystickListener()
	uri = daemon.connect(joy, "joystick")
	print("Pyro Daemon started on port %s" % daemon.port)
	print("JoystickListener at %s" % uri)

	daemon.requestLoop()

