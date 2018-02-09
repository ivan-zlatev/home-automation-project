#!/usr/bin/python

# DEFINE --SENSOR-- CLASS
class sensor:
	def __init__(self, info, address, data):
		self.sensorInfo = str(info)
		self.sensorAddress = int(address)
		self.sensorData = int(data)
	# GET --SENSOR-- ATTRIBUTES
	def getInfo(self):
		return self.sensorInfo
	def getAddress(self):
		return self.sensorAddress
	def getData(self):
		return self.sensorData
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

