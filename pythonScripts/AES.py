#!/usr/bin/python
from Crypto.Cipher import AES
import os
import binascii
from private_data import LoginCredentials

def decryptMessage( message, debug=False ):
	try:
		cipher	= AES.new(LoginCredentials['AES_SECRET'], AES.MODE_CBC, LoginCredentials['AES_IV'])
		if debug:
			print "Created cipher with the following credentials:\n\tAES_SECRET: '{}'\n\tMODE_CBC: '{}'\n\tAES_IV: '{}'".format(LoginCredentials['AES_SECRET'], AES.MODE_CBC, LoginCredentials['AES_IV'])
	except:
		print "Could not initialize AES cipher"
		return False
	try:
		decodedMessage = '{}'.format(cipher.decrypt(message))
		if debug:
			print "Decoded message: {}'".format(decodedMessage)
		return [ int(decodedMessage[8:10], 16), int(decodedMessage[10:12], 16), int(decodedMessage[12:], 16) ]
	except:
		print "Could not decrypt message"
		return False

def encryptMessage( client_addr, sensor_addr, sensor_data, debug=False ):
	try:
		cipher	= AES.new(LoginCredentials['AES_SECRET'], AES.MODE_CBC, LoginCredentials['AES_IV'])
		if debug:
			print "Created cipher with the following credentials:\n\tAES_SECRET: '{}'\n\tMODE_CBC: '{}'\n\tAES_IV: '{}'".format(LoginCredentials['AES_SECRET'], AES.MODE_CBC, LoginCredentials['AES_IV'])
	except:
		print "Could not initialize AES cipher"
		return False
	try:
		client_addr	= '{:0>2}'.format(str(client_addr).lower())[0:2]
		sensor_addr	= '{:0>2}'.format(str(sensor_addr).lower())[0:2]
		sensor_data	= '{:0>4}'.format(str(sensor_data).lower())[0:4]
		PRNG		= binascii.hexlify(os.urandom(4))
		message		= PRNG + client_addr + sensor_addr + sensor_data
		message		= message.zfill(16)
		if debug:
			print "Created a message ready for encryption:"
			print "\tclient: '{}'".format(client_addr)
			print "\tsensor: '{}'".format(sensor_addr)
			print "\tdata: '{}'".format(sensor_data)
			print "\tPRNG: '{}'".format(PRNG)
			print "\tmsg:  '{}'".format(message)
	except:
		print "Could not create message"
		return False
	try:
		ciphertext	= cipher.encrypt(message)
		return ciphertext
	except:
		print "Could not encrypt message"
		return False

