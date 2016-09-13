#!/usr/bin/python
#--------------------------------------------------------------------------------
# DEFINE --SENSOR-- CLASS -------------------------------------------------------
#--------------------------------------------------------------------------------
class sensor:
	def __init__(self, info, address, data, parentInfo, parentAddress):
		self.sensorInfo = info
		self.sensorAddress = address
		self.sensorData = data
		self.parentInfo = parentInfo
		self.parentAddress = parentAddress
#--------------------------------------------------------------------------------
# GET --SENSOR-- ATTRIBUTES -----------------------------------------------------
#--------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------
# UPDATE --SENSOR-- ATTRIBUTES --------------------------------------------------
#--------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------
# CREATE --DEVICE-- CLASS -------------------------------------------------------
#--------------------------------------------------------------------------------
class device:
	def __init__(self, info, address):
		self.deviceInfo = info
		self.deviceAddress = address
		self.deviceSensors = []
	#	if verboseOutput:
	#		print 'Device created:\n\tInfo:     {}\n\tAddress:  0x {}'.format( self.deviceInfo, self.deviceAddress )
#--------------------------------------------------------------------------------
# GET --DEVICE-- ATTRIBUTES -----------------------------------------------------
#--------------------------------------------------------------------------------
	def getInfo(self):
		return self.deviceInfo
	def getAddress(self):
		return self.deviceAddress
	def getSensors(self):
		return self.deviceSensors
#--------------------------------------------------------------------------------
# UPDATE --DEVICE-- ATTRIBUTES --------------------------------------------------
#--------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------
#  ADD SENSOR -------------------------------------------------------------------
#--------------------------------------------------------------------------------
	def addSensor(self, sensor_info, sensor_address, sensor_data):
		try:
			self.deviceSensors.append(sensor(sensor_info, sensor_address, sensor_data, self.deviceInfo, self.deviceAddress ))
	#		if verboseOutput:
	#			print 'Sensor created:\n\tDev Info: {}\n\tDev Addr: 0x {}\n\tInfo:     {}\n\tAddress:  0x {}\n\tData:     0x {}'.format(self.deviceInfo, self.deviceAddress, sensor_info, sensor_address, sensor_data)
			return self
		except:
			return False

