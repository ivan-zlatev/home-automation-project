#!/usr/bin/python
from Crypto.Cipher import AES
import os
import binascii
from private_data import LoginCredentials

def decryptMessage( message ):
	try:
		cipher	= AES.new(LoginCredentials['AES_SECRET'], AES.MODE_CBC, LoginCredentials['AES_IV'])
	except:
		print "Could not initialize AES cipher"
		return False
	try:
		decodedMessage = '{}'.format(cipher.decrypt(message))
		return [ int(decodedMessage[10:12], 16), int(decodedMessage[12:], 16) ]
	except:
		print "Could not decrypt message"
		return False

def encryptMessage( sensor_addr, sensor_data ):
	try:
		cipher	= AES.new(LoginCredentials['AES_SECRET'], AES.MODE_CBC, LoginCredentials['AES_IV'])
	except:
		print "Could not initialize AES cipher"
		return False
	try:
		sensor_addr	= '{:0>2}'.format(str(sensor_addr).lower())[0:2]
		sensor_data	= '{:0>4}'.format(str(sensor_data).lower())[0:4]
		PRNG		= binascii.hexlify(os.urandom(5))
		message		= PRNG + sensor_addr + sensor_data
		message		= message.zfill(16)
	except:
		print "Could not create message"
		return False
	try:
		ciphertext	= cipher.encrypt(message)
		return ciphertext
	except:
		print "Could not encrypt message"
		return False

