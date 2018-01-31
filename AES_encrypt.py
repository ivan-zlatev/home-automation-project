#!/usr/bin/python
from Crypto.Cipher import AES
import os
import binascii
import argparse
from array import array

parser		= argparse.ArgumentParser(description="Encrypt some sensor data.")
parser.add_argument('--device_address', dest='dev_addr', help='device address[00-ff]')
parser.add_argument('--sensor_address', dest='sensor_addr', help='sensor address[00-ff]')
parser.add_argument('--sensor_data', dest='sensor_data', help='sensor data[0000-ffff]')
args		= parser.parse_args()

#THIS IS THE ENC/DEC PART
secret		= 'this is a secret'
IV		= 'this is an iv123'
cipher_enc	= AES.new(secret, AES.MODE_CBC, IV)

dev_addr	= '{:0>2}'.format(str(args.dev_addr).lower())
sensor_addr	= '{:0>2}'.format(str(args.sensor_addr).lower())
sensor_data	= '{:0>4}'.format(str(args.sensor_data).lower())
PRNG		= binascii.hexlify(os.urandom(4))
message		= PRNG + dev_addr + sensor_addr + sensor_data
message		= message.zfill(16)

ciphertext	= cipher_enc.encrypt(message)
encoded		= '{}'.format(binascii.hexlify(ciphertext))

#print len(ciphertext)
#print array("B", ciphertext)
print encoded
#print ciphertext
