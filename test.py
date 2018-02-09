#!/usr/bin/python
import pythonScripts.CLASS as CLASS
import mysqlDB

def initializeSensors(): # DEFINE ROOMS/DEVICES/SENSORS
	rooms = { #	<room name>		<device/arduino name>			<device/arduino/parent address>
			'Bedroom1':[
				CLASS.device('Arduino Nano Bedroom 1 - Shutters ',		01),
				CLASS.device('Arduino Nano Bedroom 1 - Ceiling 1',		02),
				CLASS.device('Arduino Nano Bedroom 1 - Ceiling 2',		03)
			],
			'Bedroom2':[
				CLASS.device('Arduino Nano Bedroom 2 - Shutters ',		11),
				CLASS.device('Arduino Nano Bedroom 2 - Ceiling 1',		12),
				CLASS.device('Arduino Nano Bedroom 2 - Ceiling 2',		13)
			],
			'Livingroom':[
				CLASS.device('Arduino Nano Livingroom - Shutters',		21),
				CLASS.device('Arduino Nano Livingroom - Ceiling 1',		22),
				CLASS.device('Arduino Nano Livingroom - Ceiling 2',		23),
				CLASS.device('Arduino Nano Livingroom - TV',			24)
			],
			'Terrace':[
				CLASS.device('Arduino Nano Terrace',				31)
			],
			'Bathroom1':[
				CLASS.device('Arduino Nano Bathroom 1 - Ceiling',		41)
			],
			'Bathroom2':[
				CLASS.device('Arduino Nano Bathroom 2 - Ceiling',		51)
			],
			'Kitchen':[
				CLASS.device('Arduino Nano Kitchen - Ceiling',			61),
				CLASS.device('Arduino Nano Kitchen - Ceiling 2',		62)
			]
	}
	# Assign sensor to devices
	ID = 1
	for tmp in [	# <sensor info>			<parent address>
			[ 'Stepper motor',		01 ],
			[ 'Light meter',		01 ],
			[ 'Temperature sensor',		02 ],
			[ 'Humidity sensor',		02 ],
			[ 'Movement sensor',		02 ],
			[ 'Gas sensor',			02 ],
			[ 'Temperature sensor',		03 ],
			[ 'Humidity sensor',		03 ],
			[ 'Movement sensor',		03 ],
			[ 'Lighting status',		03 ],
			[ 'Lighting PWM',		03 ],
			[ 'Stepper motor',		11 ],
			[ 'Light meter',		11 ],
			[ 'Temperature sensor',		12 ],
			[ 'Humidity sensor',		12 ],
			[ 'Movement sensor',		12 ],
			[ 'Gas sensor',			12 ],
			[ 'Temperature sensor',		13 ],
			[ 'Humidity sensor',		13 ],
			[ 'Movement sensor',		13 ],
			[ 'Lighting status',		13 ],
			[ 'Lighting PWM',		13 ]
		]:
		for room in rooms:
			for device in rooms[room]:
				if device.getAddress() == tmp[1]:
					device.addSensor(tmp[0], ID, 0 )
					ID += 1
	return rooms

def setZeroValuesForAllSensors( sensors ):
	try:
		for room in sensors:
			for device in sensors[room]:
				for sensor in device.getSensors():
					mysqlDB.addNewRecord( sensor.getParentAddress(), sensor.getAddress(), sensor.getData() )
		return True
	except:
		print "Something went terribly wrong :)"
		return False

def readSensorValuesFromDB( sensors ):
	for room in sensors:
		for device in sensors[room]:
			for sensor in device.getSensors():
				sensor.updateData( mysqlDB.readRecord( sensor.getParentAddress(), sensor.getAddress() )[3] )

def main():
	sensors = initializeSensors()
	setZeroValuesForAllSensors( sensors )
	readSensorValuesFromDB( sensors )
	for room in sensors:
		for device in sensors[room]:
			for sensor in device.getSensors():
				print str( sensor.getParentAddress() ) + " " + str( sensor.getAddress() ) + " " + str( sensor.getData() )
	return True

#--------------------------------------------------------------------------------
#--- END --- END --- END --- END --- END --- END --- END --- END --- END --- END 
#--------------------------------------------------------------------------------
if __name__ == "__main__":
	main()

