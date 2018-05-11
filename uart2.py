import os,serial,time

import Adafruit_BBIO.UART as UART

#UART.setup("UART2")


gsm= serial.Serial(port='/dev/ttyO2',baudrate=115200,timeout=1)

while True:
	
	print "code is running \n"
	gsm.write('HI'+'\r\n')
	time.sleep(2)
	print gsm.read(50)
	time.sleep(5)
