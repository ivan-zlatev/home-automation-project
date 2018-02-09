#!/usr/bin/python

# DEFINE --SENSOR-- CLASS
class sensor:
	def __init__(self, info, address, data, parentInfo, parentAddress):
		self.sensorInfo = str(info)
		self.sensorAddress = int(address)
		self.sensorData = int(data)
		self.parentInfo = str(parentInfo)
		self.parentAddress = int(parentAddress)
	# GET --SENSOR-- ATTRIBUTES
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
	# UPDATE --SENSOR-- ATTRIBUTES
	def updateInfo(self, new_info):
		try:
			self.sensorInfo = str(new_info)
			return True
		except:
			return False
	def updateAddress(self, new_address):
		try:
			self.sensorAddress = int(new_address)
			return True
		except:
			return False
	def updateData(self, new_data):
		try:
			self.sensorData = int(new_data)
			return True
		except:
			return False
# CREATE --DEVICE-- CLASS
class device:
	def __init__(self, info, address):
		self.deviceInfo = str(info)
		self.deviceAddress = int(address)
		self.deviceSensors = []
	# GET --DEVICE-- ATTRIBUTES
	def getInfo(self):
		return self.deviceInfo
	def getAddress(self):
		return self.deviceAddress
	def getSensors(self):
		return self.deviceSensors
	# UPDATE --DEVICE-- ATTRIBUTES
	def updateInfo(self, new_info):
		try:
			self.deviceInfo = str(new_info)
			return True
		except:
			return False
	def updateAddress(self, new_address):
		try:
			self.deviceAddress = int(new_address)
			return True
		except:
			return False
	# ADD SENSOR
	def addSensor(self, sensor_info, sensor_address, sensor_data):
		try:
			self.deviceSensors.append(sensor(sensor_info, sensor_address, sensor_data, self.deviceInfo, self.deviceAddress ))
			return self
		except:
			return False

