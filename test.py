#!/usr/bin/python
import CLASS

def main():
#--------------------------------------------------------------------------------
# DEFINE ROOMS/DEVICES/SENSORS --------------------------------------------------
#--------------------------------------------------------------------------------
	verboseOutput = True
	devDB = {}
	rooms = {
		'Bedroom1':[
			CLASS.device('Arduino Nano Bedroom 1 - Shutters ', '05'),
			CLASS.device('Arduino Nano Bedroom 1 - Ceiling 1', '24'),
			CLASS.device('Arduino Nano Bedroom 1 - Ceiling 2', 'FC')
		],
		'Bedroom2':[
			CLASS.device('Arduino Nano Bedroom 2 - Shutters ', '04'),
			CLASS.device('Arduino Nano Bedroom 2 - Ceiling 1', 'F3'),
			CLASS.device('Arduino Nano Bedroom 2 - Ceiling 2', '82')
		],
		'Livingroom':[
			CLASS.device('Arduino Nano Livingroom - Shutters', '24'),
			CLASS.device('Arduino Nano Livingroom - Ceiling 1', '15'),
			CLASS.device('Arduino Nano Livingroom - Ceiling 2', '12'),
			CLASS.device('Arduino Nano Livingroom - TV', '02')
		],
		'Terrace':[
			CLASS.device('Arduino Nano Terrace', '5C')
		],
		'Bathroom1':[
			CLASS.device('Arduino Nano Bathroom 1 - Ceiling', 'C6')
		],
		'Bathroom2':[
			CLASS.device('Arduino Nano Bathroom 2 - Ceiling', '5F')
		],
		'Kitchen':[
			CLASS.device('Arduino Nano Kitchen - Ceiling', '25'),
			CLASS.device('Arduino Nano Kitchen - Ceiling 2', '6D')
		]
	}
#--------------------------------------------------------------------------------
# SENSORS FOR Bedroom 1 ---------------------------------------------------------
#--------------------------------------------------------------------------------
	for tmp in [
			['Stepper motor', '02', 'FFFF'],
			['Light meter', '5F', '0000']
		]:
		rooms['Bedroom1'][0].addSensor(tmp[0], tmp[1], tmp[2])

	for tmp in [
			['Temperature sensor', '24', '025F'],
			['Humidity sensor', '7F', '12CB'],
			['Movement sensor', '64', '63FA'],
			['Gas sensor', '25', 'AAAA']
		]:
		rooms['Bedroom1'][1].addSensor(tmp[0], tmp[1], tmp[2])
	for tmp in [
			['Temperature sensor', '25', '025E'],
			['Humidity sensor', '2A', '12CA'],
			['Movement sensor', 'FB', '1562'],
			['Lighting status', '52', '0001'],
			['Lighting PWM', '53', '1251']
		]:
		rooms['Bedroom1'][2].addSensor(tmp[0], tmp[1], tmp[2])
#--------------------------------------------------------------------------------
# SENSORS FOR Bedroom 2 ---------------------------------------------------------
#--------------------------------------------------------------------------------
	for tmp in [
			['Stepper motor', '02', 'FFFF'],
			['Light meter', '5F', '0000']
			]:
		rooms['Bedroom2'][0].addSensor(tmp[0], tmp[1], tmp[2])
	for tmp in [
			['Temperature sensor', '24', '025F'],
			['Humidity sensor', '7F', '12CB'],
			['Movement sensor', '64', '63FA'],
			['Gas sensor', '25', 'AAAA']
		]:
		rooms['Bedroom2'][1].addSensor(tmp[0], tmp[1], tmp[2])
	for tmp in [
			['Temperature sensor', '25', '025E'],
			['Humidity sensor', '2A', '12CA'],
			['Movement sensor', 'FB', '1562'],
			['Lighting status', '52', '0001'],
			['Lighting PWM', '53', '1251']
		]:
		rooms['Bedroom2'][2].addSensor(tmp[0], tmp[1], tmp[2])
#--------------------------------------------------------------------------------
# PRINT SENSORS FOR DEBUGGING ---------------------------------------------------
#--------------------------------------------------------------------------------
	for room in rooms:
		print '---------------------------------------------------------------------------------'
		print room
		for dev in rooms[room]:
			print "\t" + dev.getInfo()
			for sensor in dev.getSensors():
				print "\t\t" + sensor.getParentInfo() + "   " + sensor.getInfo() + "\t\t" + sensor.getData()




#--------------------------------------------------------------------------------
#--- END --- END --- END --- END --- END --- END --- END --- END --- END --- END 
#--------------------------------------------------------------------------------
if __name__ == "__main__":
	main()

