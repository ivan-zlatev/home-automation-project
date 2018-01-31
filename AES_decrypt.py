#!/usr/bin/python
from Crypto.Cipher import AES
import sys
import binascii

#THIS IS THE ENC/DEC PART
secret		= 'this is a secret'
IV		= 'this is an iv123'

cipher_dec	= AES.new(secret, AES.MODE_CBC, IV)

for line in sys.stdin:
	#print binascii.hexlify(line)
	line = line[:-1]
	#print binascii.hexlify(line)
	print 'Received string:\t{}'.format(line)
	decoded_text ='{}'.format(cipher_dec.decrypt(binascii.unhexlify(line)))
	print 'Decoded string:\t\t{}'.format(decoded_text)
	print 'Device Address:\t\t{}'.format(decoded_text[8:10])
	print 'Sensor Address:\t\t{}'.format(decoded_text[10:12])
	print 'Sensor Data:\t\t{}'.format(decoded_text[12:])

