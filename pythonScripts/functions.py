#!/usr/bin/python
import MySQL
#import nrf24 # from https://github.com/jpbarraca/pynrf24
#import spidev

def populateLedger():
	# Create control devices
	sensors = {}
	i = 1
	for name in [
			'1: Stepper motor',
			'2: Light meter',
			'2: Temperature sensor',
			'2: Humidity sensor',
			'2: Movement sensor',
			'2: Gas sensor',
			'3: Temperature sensor',
			'3: Humidity sensor',
			'3: Movement sensor',
			'3: Lighting status',
			'3: Lighting PWM',
			'4: Stepper motor',
			'4: Light meter',
			'5: Temperature sensor',
			'5: Humidity sensor',
			'5: Movement sensor',
			'5: Gas sensor',
			'6: Temperature sensor',
			'6: Humidity sensor',
			'6: Movement sensor',
			'6: Lighting status',
			'6: Lighting PWM',
		]:
		print "Adding sensor: '{}', '{}', '{}'".format( name[0], i, name[3:])
		sensorAddress = MySQL.addSensor( name[0], i, name[3:] )
		MySQL.addData( name[0], i, 0 )
		i += 1

populateLedger()

