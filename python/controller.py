#!/usr/bin/python
import serial
import rockets

CONTROLS = { 'fwd'	: 'F',
	      'rev'	: 'B',
	      'right'	: 'R',
	      'left'	: 'L'   }

MOVE_COMMANDS = { ' ' : 'stop',
		 'i' : 'fwd',
		 'k' : 'rev',
		 'j' : 'left',
		 'l' : 'right'  }

SPEED_COMMANDS = { 's' : -1,
		   'd' : +1,
		   'f' : -25,
		   'g' : +25  }

DIGITS = map(str,range(10))
PORT = serial.Serial("/dev/arduino1",baudrate=57600,bytesize=serial.EIGHTBITS)

class Getch:
        def __init__(self):
                import tty, sys

        def __call__(self):
                import sys, tty, termios
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                        tty.setraw(sys.stdin.fileno())
                        ch = sys.stdin.read(1)
                finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch

#MYGETCH = Getch()

def setOutput(data):
	PORT.write(data)
	PORT.write("Pz")
#	print 'Output set to:', data[0], ord(data[1])
#       printHelp()

def setDrive(value):
	if value == 'A':
		setOutput('DA')
	if value == 'B':
		setOutput('DB')

def moveBot(dir, speed):
	output = CONTROLS[dir] + chr(speed)
	setOutput(output)

def stopBot():
	setOutput('SS')

def setSpeed(value):
	global speed
	speed = value
	if speed > 255:
		speed = 255
	if speed < 0:
		speed = 0
	print 'speed:', speed, '/ 255'


def handleCommand(cmd):
	global speed
	if cmd in DIGITS: # 0-9
		setSpeed(int(cmd)*255/9)
	if cmd in SPEED_COMMANDS.keys():
		setSpeed(speed + SPEED_COMMANDS[cmd])
	elif cmd in MOVE_COMMANDS.keys():
		if MOVE_COMMANDS[cmd] == 'stop':
			stopBot()
		else:
			print MOVE_COMMANDS[cmd]
			moveBot(MOVE_COMMANDS[cmd], speed)
	elif cmd == 'w':
		rockets.up()
	elif cmd == 'e':
		rockets.down()
        elif cmd == 'q':
                rockets.left()
        elif cmd == 'r':
                rockets.right()	
	elif cmd == 't':
		rockets.laser()
	elif cmd == 'y':
		rockets.fire()
	elif cmd == 'a':
		setDrive('A')
	elif cmd == 'b':
		setDrive('B')
 
def printHelp():
	print 'commands: '
	print 'i j k l to move, SPACE = stop, x = quit'
	print 's d f g or 0-9 to adjust speed between 0 and 255.'

import termios, select, sys, tty

def isData():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def main():
	while True:
		PORT.write("Pz")
		cmd = "" #cmd = MYGETCH()
		if isData():
			cmd = sys.stdin.read(1)
			if cmd == 'x':
				break
			if len(cmd) > 0:
				handleCommand(cmd)
				#if cmd == '?':
				printHelp()
		#if PORT.inWaiting() > 0:
		#	print PORT.readline()


old_settings = termios.tcgetattr(sys.stdin)
stopBot()
speed = 0
if __name__ == "__main__":
	try:
		tty.setcbreak(sys.stdin.fileno())
		main()
	finally:
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
