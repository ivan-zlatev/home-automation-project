#!/usr/bin/python
from Crypto.Cipher import AES
import os
import binascii


#THIS IS THE ENC/DEC PART
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
	print "----------------------------------------------------------"

