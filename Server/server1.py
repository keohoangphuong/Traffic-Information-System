
import time
import sys
import os, json
import pprint
import uuid
from uuid import getnode as get_mac


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
	print("Received live data from %s (%s) sent at %s: %s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), json.dumps(event.data)))
		

#####################################
#FILL IN THESE DETAILS
#####################################     
organization = "objday"
deviceType = "Raspberrypi3"
deviceId = "raspi3"
appId = str(uuid.uuid4())
authMethod = "token"
authToken = "hoangvuong"

##API TOKEN AND KEY
authkey = "a-objday-hf2z9pfccj"
authtoken = "Of)ahqGMDv-nA?99X6"
# Initialize the application client.

try:
	appOptions = {"org": organization, "id": appId,"auth-method": "apikey", "auth-key" : authkey, "auth-token":authtoken }
	

except Exception as e:
	print(str(e))
	sys.exit()

# Connect and configuration the application
# - subscribe to live data from the device we created, specifically to "greeting" events
# - use the myAppEventCallback method to process events
while(True):
	raw_input("Enter local ID: ")
	print("Chose command: \n")
	print("  1: Set speed.  \n")
	print("  2: Hork control  \n")
	print("  3: Road maintenance  \n")
	command = raw_input("Enter: ")

	if command == '1':
		opt1 = raw_input("Enter speed rule: ")
		command = "SL" + opt1 + "00"
		try:
			appCli = ibmiotf.application.Client(appOptions)
			appCli.connect()
			commandData={'rule' : command}
		
			appCli.publishCommand(deviceType, deviceId,command ,"json", commandData)
			appCli.publishEvent(deviceType, deviceId,command,"json", commandData)
			x=0
			while(x<1):
				appCli.deviceEventCallback = myAppEventCallback
				appCli.subscribeToDeviceEvents(event="status")
				x=x+1
				
		except Exception as e:
			print ("Connect attempt failed: "+str(e))
			sys.exit()


	elif command == '2':
		opt2 = raw_input("Enter hork control [y/n]: ")
		if opt2=="y":
			command = "SL6010"
		else:
			command = "SL6000"
		try:
			appCli = ibmiotf.application.Client(appOptions)
			appCli.connect()
			commandData={'rule' : command}
		
			appCli.publishCommand(deviceType, deviceId, command,"json", commandData)
			appCli.publishEvent(deviceType, deviceId,command,"json", commandData)
			y=0
			while(y<1):
				appCli.deviceEventCallback = myAppEventCallback
				appCli.subscribeToDeviceEvents(event="status")
				y=y+1
		except Exception as e:
			print ("Connect attempt failed: "+str(e))
			sys.exit()
	
	elif command == '3':
		opt2 = raw_input("Enter road maintenance status [y/n]: ")
		if opt2=="y":
			command = "SL6001"
		else:
			command = "SL6000"
		try:
			appCli = ibmiotf.application.Client(appOptions)
			appCli.connect()
			commandData={'rule' : command}
		
			appCli.publishCommand(deviceType, deviceId, command,"json", commandData)
			appCli.publishEvent(deviceType, deviceId,command,"json", commandData)
			y=0
			while(y<1):
				appCli.deviceEventCallback = myAppEventCallback
				appCli.subscribeToDeviceEvents(event="status")
				y=y+1	
			
		except Exception as e:
			print ("Connect attempt failed: "+str(e))
			sys.exit()


	else:
		print ("Not a valid command")
appCli.disconnect()

