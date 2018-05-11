import os,serial,time

gsm= serial.Serial(port='/dev/ttyUSB3',baudrate=115200,timeout=1)

while True:

        try:

                print "gsm test"

                gsm.write("AT"+"\r\n")

                print gsm.read(100)

                time.sleep(1)

                gsm.write("AT+CSQ"+"\r\n")

                print gsm.read(100)

                time.sleep(1)

                gsm.write("AT+CGPS=1"+"\r\n")

                print gsm.read(100)

                #gsm.write("AT+CGPSINFO"+"\r\n")

                #print gsm.read(100)
		
		gsm.write("AT+CGPSINFOCFG=?\r\n")
		print gsm.read(100)
		time.sleep(1)
		
		gsm.write("AT+CGPSINFOCFG=10,2\r\n")
		print gsm.read(100)
		time.sleep(1)


        except:
		print "exception"
		time.sleep(1)
