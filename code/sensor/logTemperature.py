#!/usr/bin/python

import sqlite3 as mydb
import sys
import os
import time

""" Log Current Time, Temperature in Celsius and Fahrenheit
    Returns a ist [time,tempC,tempF]"""

def readTemp():
    tempfile = open("/sys/bus/w1/devices/28-0000069634cc/w1_slave")
    tempfile_text = tempfile.read()
    currentTime = time.strftime('%x %X %Z')
    tempfile.close()
    tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
    tempF = tempC*9.0/5.0+32.0
    print "Current temperature is: " + str(tempC) + " C , " + str(tempF) + " F"
    
readTemp()

con = None
try:
    con = mydb.connect('temperature.db')
    cur = con.cursor()    
    cur.execute("INSERT INTO Temp VALUES(?, ?, ?)", (currentTime, tempC, tempF))
    con.commit
    print  "Temperature Logged"
                   
except mydb.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()

