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

def addData( client, address, data ):
	try:
		sql	= "INSERT INTO " + LoginCredentials['mysql_table_data'] + " ( epoch, client, address, data ) VALUES ( %d, %d, %d, %d )" % (int(time.time()), int(str(client), 16), int(str(address), 16), int(str(data), 16))
		cursor.execute(sql)
		db.commit()
		return True
	except:
		return False

def getData( client, address ):
	try:
		sql	= "SELECT * FROM " + LoginCredentials['mysql_table_data'] + " WHERE address = " + str(int(str(address), 16)) + " AND client = " + str(int(str(client), 16)) + " ORDER BY epoch DESC"
		cursor.execute(sql)
		return cursor.fetchall()[0]
	except:
		return False

def addSensor( client, address, name ):
	try:
		sql	= "INSERT INTO " + LoginCredentials['mysql_table_ledger'] + " ( client, address, name ) VALUES ( %d, %d, '%s' )" % (int(str(client), 16), int(str(address), 16), str(name))
		cursor.execute(sql)
		db.commit()
		return int(cursor.lastrowid)
	except:
		return False

def getSensor( client, address ):
	try:
		sql	= "SELECT name FROM " + LoginCredentials['mysql_table_ledger'] + " WHERE address = " + str(int(str(address), 16)) + " AND client = " + str(int(str(client), 16)) + ""
		cursor.execute(sql)
		return cursor.fetchone()[0]
	except:
		return False

