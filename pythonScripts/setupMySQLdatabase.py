#!/usr/bin/python

import MySQLdb
from private_data import LoginCredentials # import credentials

try:
	db	= MySQLdb.connect(
			host=LoginCredentials['mysql_host'],
			user=LoginCredentials['mysql_username'],
			passwd=LoginCredentials['mysql_password'],
		) # connect to the MySQL server
except:
	print "Could not connect to the MySQL database"
	return False
try:
	cursor	= db.cursor()
	sql	= "CREATE DATABASE " + LoginCredentials['mysql_db'] # Create a new database
	cursor.execute(sql)
except:
	print "Could not create database entry"
	return False
try:
	db.select_db(LoginCredentials['mysql_db']) # USE that database
	cursor	= db.cursor()
	table	= LoginCredentials['mysql_table']
	sql	= "CREATE TABLE " + table + "( epoch int, parent_id int, sensor_id int, sensor_data int )"
	cursor.execute(sql)
	db.commit()
	return True
except:
	print "Could not create table entry"
	return False

# The columns are as follows:
#
#	epoch		epoch time when the data was collected
#	parent_id	parent address (arduino address) [0-255]
#	sensor_id	sensor address [0-255]
#	sensor_data	sensor data [0-65535]
#

