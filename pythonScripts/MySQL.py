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

def addData( address, data ):
	try:
		sql	= "INSERT INTO " + LoginCredentials['mysql_table_data'] + " ( epoch, address, data ) VALUES ( %d, %d, %d )" % (int(time.time()), address, data)
		cursor.execute(sql)
		db.commit()
		return True
	except:
		return False

def getData( address ):
	try:
		sql	= "SELECT * FROM " + LoginCredentials['mysql_table_data'] + " WHERE address = " + str(int(address)) + " ORDER BY epoch DESC"
		cursor.execute(sql)
		return cursor.fetchall()[0]
	except:
		return False

def addSensor( name ):
	try:
		sql	= "INSERT INTO " + LoginCredentials['mysql_table_ledger'] + " ( name ) VALUES ( '%s' )" % (str(name))
		cursor.execute(sql)
		db.commit()
		return int(cursor.lastrowid)
	except:
		return False

def getSensor( address ):
	try:
		sql	= "SELECT name FROM " + LoginCredentials['mysql_table_ledger'] + " WHERE id = " + str(int(address)) + " ORDER BY id DESC"
		cursor.execute(sql)
		return cursor.fetchone()[0]
	except:
		return False

