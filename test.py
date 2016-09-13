from Crypto.Cipher import AES
import os
import binascii


''' #THIS IS THE ENC/DEC PART
secret = 'this is a secret'
IV = 'this is an iv123'

cipher_enc = AES.new(secret, AES.MODE_CBC, IV)
cipher_dec = AES.new(secret, AES.MODE_CBC, IV)

dev_addr = '{:0>2}'.format('11')
sensor_addr = '{:0>2}'.format('22')

for i in range(0, int("ff", 16)+1, 20):
	i = '%x' % i
	sensor_data = '{:0>4}'.format(i)
	PRNG = binascii.hexlify(os.urandom(4))
	message = PRNG + dev_addr + sensor_addr + sensor_data
	message = message.zfill(16)
	print 'Message string: {}'.format(message)
	print '  PRNG:  {}\n  Device:  {}\n  Sensor:  {}\n  Data:  {}'.format(PRNG, dev_addr, sensor_addr, sensor_data)
	ciphertext = cipher_enc.encrypt(message)
	print 'Encoded string: {}'.format(binascii.hexlify(ciphertext))
	print 'Decoded string: {}'.format(cipher_dec.decrypt(ciphertext))
	print ""
'''
def main(verboseOutput=False):

	# define device/sensor classes
	class sensor:
		def __init__(self, info, address, data, parentInfo, parentAddress):
			self.sensorInfo = info
			self.sensorAddress = address
			self.sensorData = data
			self.parentInfo = parentInfo
			self.parentAddress = parentAddress
	
		#get sensor attributes
		def getInfo(self):
			return self.sensorInfo
		def getAddress(self):
			return self.sensorAddress
		def getData(self):
			return self.sensorData
		def getParentInfo(self):
			return self.parentInfo
		def getParentAddress(self):
			return self.parentAddress
	
		#update sensor attributes
		def updateInfo(self, new_info):
			try:
				self.sensorInfo = new_info
				return True
			except:
				return False
		def updateAddress(self, new_address):
			try:
				self.sensorAddress = new_address
				return True
			except:
				return False
		def updateData(self, new_data):
			try:
				self.sensorData = new_data
				return True
			except:
				return False
	
	
	class device:
		def __init__(self, info, address):
			self.deviceInfo = info
			self.deviceAddress = address
			self.deviceSensors = []
			if verboseOutput:
				print 'Device created:\n\tInfo:     {}\n\tAddress:  0x {}'.format( self.deviceInfo, self.deviceAddress )
	
		#get device attributes
		def getInfo(self):
			return self.deviceInfo
		def getAddress(self):
			return self.deviceAddress
		def getSensors(self):
			return self.deviceSensors
		def getSensorsAddr(self):
			tmp = []
			for i in self.getSensors():
				tmp.append(i[0])
			return tmp
	
		#update device attributes
		def updateInfo(self, new_info):
			try:
				self.deviceInfo = new_info
				return True
			except:
				return False
		def updateAddress(self, new_address):
			try:
				self.deviceAddress = new_address
				return True
			except:
				return False
	
		# sensors
		def addSensor(self, sensor_info, sensor_address, sensor_data):
			try:
				self.deviceSensors.append(sensor(sensor_info, sensor_address, sensor_data, self.deviceInfo, self.deviceAddress ))
				if verboseOutput:
					print 'Sensor created:\n\tDev Info: {}\n\tDev Addr: 0x {}\n\tInfo:     {}\n\tAddress:  0x {}\n\tData:     0x {}'.format(self.deviceInfo, self.deviceAddress, sensor_info, sensor_address, sensor_data)
				return self
			except:
				return False
#		def getSensor(self, sensor_address):
#			for i in self.deviceSensors:
#				if i[0] == sensor_address:
#					return i[1]
#			print 'sensor not found!'
#			return None
	
	# create devices/sensors
	
	#devDB = {}
	#devDB['00'] = device('Arduino Nano Kitchen', 'AC')
	#devDB['01'] = device('Arduino Nano Bedroom 1', 'F1')
	#
	#print ""
	#
	#sensor1 = devDB['01'].addSensor('Humidity meter', '0C', '0C29')
	#sensor2 = devDB['01'].addSensor('Temperature meter', 'FA', '16FA')

	devDB = {}
	rooms = {
		'Bedroom1':{
			'1' : device('Arduino Nano Bedroom 1 - Shutters ', '05'),
			'2' : device('Arduino Nano Bedroom 1 - Ceiling 1', '24'),
			'3' : device('Arduino Nano Bedroom 1 - Ceiling 2', 'FC')
		},
		'Bedroom2':{
			'1' : device('Arduino Nano Bedroom 2 - Shutters ', '04'),
			'2' : device('Arduino Nano Bedroom 2 - Ceiling 1', 'F3'),
			'3' : device('Arduino Nano Bedroom 2 - Ceiling 2', '82')
		},
		'Livingroom':{
			'1' : device('Arduino Nano Livingroom - Shutters', '24'),
			'2' : device('Arduino Nano Livingroom - Ceiling 1', '15'),
			'3' : device('Arduino Nano Livingroom - Ceiling 2', '12'),
			'4' : device('Arduino Nano Livingroom - TV', '02')
		},
		'Terrace':{
			'1' : device('Arduino Nano Terrace', '5C')
		},
		'Bathroom1':{
			'1' : device('Arduino Nano Bathroom 1 - Ceiling', 'C6')
		},
		'Bathroom2':{
			'1' : device('Arduino Nano Bathroom 2 - Ceiling', '5F')
		},
		'Kitchen':{
			'1' : device('Arduino Nano Kitchen - Ceiling', '25'),
			'2' : device('Arduino Nano Kitchen - Ceiling 2', '6D')
		}
	}

	for tmp in [
			['Stepper motor', '02', 'FFFF'],
			['Light meter', '5F', '0000']
		]:
		rooms['Bedroom1']['1'].addSensor(tmp[0], tmp[1], tmp[2])

	for tmp in [
			['Temperature sensor', '24', '025F'],
			['Humidity sensor', '7F', '12CB'],
			['Movement sensor', '64', '63FA'],
			['Gas sensor', '25', 'AAAA']
		]:
		rooms['Bedroom1']['2'].addSensor(tmp[0], tmp[1], tmp[2])
	for tmp in [
			['Temperature sensor', '25', '025E'],
			['Humidity sensor', '2A', '12CA'],
			['Movement sensor', 'FB', '1562'],
			['Lighting status', '52', '0001'],
			['Lighting PWM', '53', '1251']
		]:
		rooms['Bedroom1']['3'].addSensor(tmp[0], tmp[1], tmp[2])
        for tmp in [
                        ['Stepper motor', '02', 'FFFF'],
                        ['Light meter', '5F', '0000']
                ]:
                rooms['Bedroom2']['1'].addSensor(tmp[0], tmp[1], tmp[2])

        for tmp in [
                        ['Temperature sensor', '24', '025F'],
                        ['Humidity sensor', '7F', '12CB'],
                        ['Movement sensor', '64', '63FA'],
                        ['Gas sensor', '25', 'AAAA']
                ]:
                rooms['Bedroom2']['2'].addSensor(tmp[0], tmp[1], tmp[2])
        for tmp in [
                        ['Temperature sensor', '25', '025E'],
                        ['Humidity sensor', '2A', '12CA'],
                        ['Movement sensor', 'FB', '1562'],
                        ['Lighting status', '52', '0001'],
                        ['Lighting PWM', '53', '1251']
                ]:
                rooms['Bedroom2']['3'].addSensor(tmp[0], tmp[1], tmp[2])


	for room in rooms:
		print '-----------------------------------------------------------------------------------------------------'
		print room
		for device in rooms[room].values():
			print "\t" + device.getInfo()
			for sensor in device.getSensors():
				print "\t\t" + sensor.getParentInfo() + "   " + sensor.getInfo() + "\t\t" + sensor.getData()









if __name__ == "__main__":
	main(verboseOutput=False)

