
import time
import sys
import serial
import pprint
import uuid
import json
import os
from uuid import getnode as get_mac

import RPi.GPIO as GPIO
import time

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)
ser.close()
ser.open()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
ls='NO'

def getCPUtemp():
	res=os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

try:
	import ibmiotf.application
	import ibmiotf.device
except ImportError:
	# This part is only required to run the sample from within the samples
	# directory when the module itself is not installed.
	#
	# If you have the module installed, just use "import ibmiotf.application" & "import ibmiotf.device"
	import os
	import inspect
	cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../src")))
	if cmd_subfolder not in sys.path:
		sys.path.insert(0, cmd_subfolder)
	import ibmiotf.application
	import ibmiotf.device


def myAppEventCallback(event):
	print("Received live data from %s (%s) sent at %s: hello=%s x=%s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), data['hello'], data['x']))

def myCommandCallback(cmd):
        #if cmd.command == "on":
        ser.write(cmd.command)
        print(cmd.command)
        GPIO.output(5,1)
        time.sleep(0.1)
        GPIO.output(5,0)
        time.sleep(0.1)
        GPIO.output(5,1)
        time.sleep(0.1)
        GPIO.output(5,0)

print       
#####################################
#
#####################################     
organization = "objday"
deviceType = "Raspberrypi3"
deviceId = "raspi3"
appId = str(uuid.uuid4())
authMethod = "token"
authToken = "hoangvuong"

# Initialize the device client.
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
	print(str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
deviceCli.commandCallback = myCommandCallback
#x=0
while(1):
        cmd = ser.read(2)
        if cmd=="LS":
                GPIO.output(5,1)
                time.sleep(0.1)
                GPIO.output(5,0)
                time.sleep(0.1)
                GPIO.output(5,1)
                time.sleep(0.1)
                GPIO.output(5,0)
                ls = "YES"              
                content=ser.read(1)
                data={'REQUEST': ls, 'LEVEL': content}
                deviceCli.publishEvent("status","json", data)
                
        else:
                ls = "NO"
                content=0
        temp=float(getCPUtemp())
        data={'Temp': temp}
        deviceCli.publishEvent("status","json", data)
        time.sleep(1)
    	

# Disconnect the device and application from the cloud
deviceCli.disconnect()
#appCli.disconnect()

