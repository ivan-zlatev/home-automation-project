#!/usr/bin/python

import MySQLdb
import time
from private_data import LoginCredentials # import credentials

db = MySQLdb.connect(	host=LoginCredentials['mysql_host'],
			user=LoginCredentials['mysql_username'],
			passwd=LoginCredentials['mysql_password'],
			db=LoginCredentials['mysql_db']
			) # connect to the MySQL server
cursor	= db.cursor()

def addNewRecord( parent_id, sensor_id, sensor_data ):
	try:
		sql	= "INSERT INTO " + LoginCredentials['mysql_table'] + " ( epoch, parent_id, sensor_id, sensor_data ) VALUES ( %d, '%s', %d, %d )" % ( int(time.time()), parent_id, sensor_id, sensor_data )
		cursor.execute(sql)
		db.commit()
		return True
	except:
		return False

def readRecord( parent_id, sensor_id ):
	try:
		sql	= "SELECT * FROM " + LoginCredentials['mysql_table'] + " WHERE parent_id = " + str( parent_id ) + " AND sensor_id = " + str( sensor_id ) + " ORDER BY epoch DESC"
		cursor.execute(sql)
		return cursor.fetchall()[0]
	except:
		return False
