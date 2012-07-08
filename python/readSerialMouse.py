#!/usr/bin/python
import serial

def int2bin(n, count=8):
        return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def signed(n, count=8):
        mask = 1 << count-1
        return ((n & mask)>> count-1) * -1*pow(2, count-1) + (n & ~mask)

def bittest(n, bit=0):
        if n & (1 << bit):
                return True
        return False

def parseMousePacket((b0,b1,b2)):
	y = (b0 & 0b1100) << 4 | (b2 & 0b111111)
	x = (b0 & 0b0011) << 6 | (b1 & 0b111111)
	return (x,y)
                        
def getSerialPort():
	p = serial.Serial("/dev/ttyS0",baudrate=1200,bytesize=serial.SEVENBITS)
        p.open()
	return p

def getNextPacket(port):
	while(1):
		b0 = ord(p.read(1))
		if bittest(b0,6):
			b1 = ord(p.read(1))
			b2 = ord(p.read(1))
			if bittest(b1,6) or bittest(b2,6):
				print "bad packet"
				continue
			return (b0,b1,b2)
	
if __name__ == "__main__":
	p = getSerialPort()	
	while(1):
		(b0,b1,b2) = getNextPacket(p)
		(x,y) = parseMousePacket([b0,b1,b2])
		#print "b0: %s\tb1: %s\tb2: %s" % (int2bin(b0),int2bin(b1),int2bin(b2))
		#print "b0: %d\t\tb1: %d\t\tb2: %d" % (b0,b1,b2)
		#print "x: %s\ty: %s" % (int2bin(x),int2bin(y))
		print "x: %d\t\ty: %d" % (signed(x),signed(y))
