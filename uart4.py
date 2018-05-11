import os,serial,time

gsm= serial.Serial(port='/dev/ttyS4',baudrate=115200,timeout=1)

while True:
	
	print "code is running \n"
	gsm.write('HI'+'\r\n')
	time.sleep(2)
	print gsm.read(50)
	time.sleep(5)
