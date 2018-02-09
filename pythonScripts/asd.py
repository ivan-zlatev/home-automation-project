#!/usr/bin/python
import CLASS as CLASS
import MySQL

def populateLedger():
	# Create control devices
	for name in [
			'ROOM 1: Stepper motor',
			'ROOM 2: Light meter',
			'ROOM 2: Temperature sensor',
			'ROOM 2: Humidity sensor',
			'ROOM 2: Movement sensor',
			'ROOM 2: Gas sensor',
			'ROOM 3: Temperature sensor',
			'ROOM 3: Humidity sensor',
			'ROOM 3: Movement sensor',
			'ROOM 3: Lighting status',
			'ROOM 3: Lighting PWM',
			'ROOM 4: Stepper motor',
			'ROOM 4: Light meter',
			'ROOM 5: Temperature sensor',
			'ROOM 5: Humidity sensor',
			'ROOM 5: Movement sensor',
			'ROOM 5: Gas sensor',
			'ROOM 6: Temperature sensor',
			'ROOM 6: Humidity sensor',
			'ROOM 6: Movement sensor',
			'ROOM 6: Lighting status',
			'ROOM 6: Lighting PWM',
		]:
		MySQL.addSensor( name )

def setZeroValuesForAllSensors( sensors ):
	try:
		for room in sensors:
			for device in sensors[room]:
				for sensor in device.getSensors():
					MySQL.addRecord( sensor.getParentAddress(), sensor.getAddress(), sensor.getData() )
		return True
	except:
		print "Something went terribly wrong :)"
		return False

