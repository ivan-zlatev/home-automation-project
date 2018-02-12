#!/usr/bin/python

import MySQLdb
import sys
from private_data import LoginCredentials # import credentials

try:
	db	= MySQLdb.connect(
			host=LoginCredentials['mysql_host'],
			user=LoginCredentials['mysql_username'],
			passwd=LoginCredentials['mysql_password'],
		) # connect to the MySQL server
	print "Connected to the MySQL server ..."
except:
	print "Could not connect to the MySQL server"
	sys.exit(0)
try:
	cursor		= db.cursor()
	sql		= "CREATE DATABASE " + LoginCredentials['mysql_db'] # Create a new database
	cursor.execute(sql)
	print "Created MySQL database [{}] ...".format(LoginCredentials['mysql_db'])
except:
	print "Could not create database entry"
	sys.exit(0)
try:
	db.select_db(LoginCredentials['mysql_db']) # USE that database
	cursor		= db.cursor()
	sql		= "CREATE TABLE " + LoginCredentials['mysql_table_data'] + "( epoch int, address smallint, data int )"
	cursor.execute(sql)
	db.commit()
	print "Created data table [{}] ...".format(LoginCredentials['mysql_table_data'])
except:
	print "Could not create data table entry"
	sys.exit(0)
try:
	cursor		= db.cursor()
	sql		= "CREATE TABLE " + LoginCredentials['mysql_table_ledger'] + "( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(255) )"
	cursor.execute(sql)
	db.commit()
	print "Created ledger table [{}] ...".format(LoginCredentials['mysql_table_ledger'])
except:
	print "Could not create ledger table entry"
	sys.exit(0)

# The columns are as follows:
#	data table:
#		epoch		epoch time when the entry was collected
#		address		sensor address [0-255]
#		data		sensor data [0-65535]
#	ledger table:
#		id		sensor address [0-255]
#		name		sensor information [varchar/string]

